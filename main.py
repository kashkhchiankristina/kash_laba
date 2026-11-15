"""Демонстрация работы модульного приложения (запуск: python main.py)."""

from num_series import (
    random_series,
    sine_series,
    trend_series,
    summarize,
    simple_moving_average,
    centered_moving_average,
    exponential_moving_average,
)


def print_series(title, values, fmt="{:>10.3f}"):
    print(f"\n{title} (n={len(values)}):")
    print("  " + " ".join(fmt.format(v) for v in values))


def print_stats(stats):
    print(f"Среднее арифметическое : {stats['mean']:>10.4f}")
    print(f"Медиана                : {stats['median']:>10.4f}")
    print(f"Размах (max - min)     : {stats['spread']:>10.4f}")
    print(f"min / max              : {stats['min']:>10.4f} / {stats['max']:.4f}")


def main():
    # 1. Источник данных (generator.py)
    data = sine_series(20, amplitude=10.0, frequency=2.0, noise=1.5, seed=42)

    # 2. Аналитика (stats.py)
    stats = summarize(data)

    # 3. Сглаживание (moving_average.py)
    sma = simple_moving_average(data, 3)
    cma = centered_moving_average(data, 5)
    ema = exponential_moving_average(data, 0.3)

    # 4. Вывод
    print("=" * 60)
    print("Тип ряда: sine, n = 20")
    print("-" * 60)
    print_stats(stats)
    print_series("Исходный ряд", data)
    print_series("SMA (window=3)", sma)
    print_series("Центрированное MA (window=5)", cma)
    print_series("EMA (alpha=0.3)", ema)
    print("=" * 60)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
