from __future__ import annotations

import argparse
import sys
from typing import List, Optional

from num_series import (
    uniform_series,
    summarize,
    simple_moving_average,
    exponential_moving_average,
    benchmark_moving_average,
)


def print_series_preview(title: str, values: List[float], limit: int = 10) -> None:
    """Печатает первые и последние элементы длинного ряда."""
    print(f"\n{title} (n={len(values)}):")
    if len(values) <= limit:
        print("  " + " ".join(f"{v:>9.3f}" for v in values))
    else:
        head = " ".join(f"{v:>9.3f}" for v in values[:5])
        tail = " ".join(f"{v:>9.3f}" for v in values[-5:])
        print(f"  {head}  ...  {tail}")


def print_stats(stats: dict) -> None:
    print(f"Среднее арифметическое : {stats['mean']:>12.4f}")
    print(f"Медиана                : {stats['median']:>12.4f}")
    print(f"Размах (max - min)     : {stats['spread']:>12.4f}")
    print(f"min / max              : {stats['min']:>12.4f} / {stats['max']:.4f}")
    print(f"Выборочная дисперсия   : {stats['variance']:>12.4f}")
    print(f"Выборочное СКО         : {stats['stdev']:>12.4f}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Вариант 1: Равномерное распределение [0, 100), дисперсия, СКО, SMA и EMA",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--n", type=int, default=1000, help="длина ряда")
    parser.add_argument("--window", "-k", type=int, default=10, help="размер окна k")
    parser.add_argument("--seed", type=int, default=42, help="зерно ГПСЧ")
    parser.add_argument(
        "--negative-test",
        action="store_true",
        help="проверка краевого кейса на диапазоне [-100, 0)",
    )
    parser.add_argument(
        "--benchmark",
        action="store_true",
        help="замерить время выполнения SMA (list vs deque)",
    )
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    low, high = (-100.0, 0.0) if args.negative_test else (0.0, 100.0)

    try:
        data = uniform_series(n=args.n, low=low, high=high, seed=args.seed)
        stats = summarize(data)

        alpha = 2.0 / (args.window + 1)
        sma = simple_moving_average(data, args.window)
        ema = exponential_moving_average(data, alpha)
    except ValueError as err:
        print(f"Ошибка: {err}", file=sys.stderr)
        return 1

    print("=" * 65)
    print(f"Равномерное распределение [{low}, {high}), n={args.n}, k={args.window}, seed={args.seed}")
    print("-" * 65)
    print_stats(stats)

    print_series_preview("Исходный ряд", data)
    print_series_preview(f"SMA (k={args.window})", sma)
    print_series_preview(f"EMA (alpha={alpha:.4f})", ema)

    if args.benchmark:
        print("-" * 65)
        timings = benchmark_moving_average(data, args.window, repeats=1000)
        print(f"SMA list  : {timings['list']:.8f} с")
        print(f"SMA deque : {timings['deque']:.8f} с")
        print(f"Отношение : {timings['list'] / timings['deque']:.2f}x")

    print("=" * 65)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
