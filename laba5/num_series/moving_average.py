from __future__ import annotations

import time
from collections import deque
from typing import Dict, List, Sequence


def _ensure_not_empty(data: Sequence[float]) -> None:
    if not data:
        raise ValueError("Ряд пуст: расчёт скользящей средней невозможен")


def check_window(window: int, n: int) -> None:
    if not isinstance(window, int) or isinstance(window, bool):
        raise ValueError(f"window должен быть целым, получено: {window!r}")
    if window < 1:
        raise ValueError(f"window должен быть >= 1, получено: {window}")
    if window > n:
        raise ValueError(f"window ({window}) больше длины ряда ({n}) — SMA невозможна")


def _check_alpha(alpha: float) -> None:
    if not (0 < alpha <= 1):
        raise ValueError(f"alpha должен быть в (0, 1], получено: {alpha}")


def simple_moving_average(data: Sequence[float], window: int) -> List[float]:
    """SMA через бегущую сумму (O(n))."""
    _ensure_not_empty(data)
    check_window(window, len(data))

    running = sum(data[:window])
    result = [running / window]
    for i in range(window, len(data)):
        running += data[i] - data[i - window]
        result.append(running / window)
    return result


def simple_moving_average_deque(data: Sequence[float], window: int) -> List[float]:
    """SMA с использованием collections.deque."""
    _ensure_not_empty(data)
    check_window(window, len(data))

    buf: deque[float] = deque(maxlen=window)
    running = 0.0
    result: List[float] = []

    for i, x in enumerate(data):
        if len(buf) == window:
            running -= buf[0]
        buf.append(x)
        running += x
        if i >= window - 1:
            result.append(running / window)
    return result


def exponential_moving_average(data: Sequence[float], alpha: float) -> List[float]:
    """Экспоненциальная скользящая средняя (EMA)."""
    _ensure_not_empty(data)
    _check_alpha(alpha)

    prev = float(data[0])
    result = [prev]
    for x in data[1:]:
        prev = alpha * x + (1.0 - alpha) * prev
        result.append(prev)
    return result


def benchmark_moving_average(
    data: Sequence[float],
    window: int,
    repeats: int = 1000,
) -> Dict[str, float]:
    """Замер среднего времени выполнения SMA на list и deque."""
    _ensure_not_empty(data)
    check_window(window, len(data))

    t0 = time.perf_counter()
    for _ in range(repeats):
        simple_moving_average(data, window)
    t_list = (time.perf_counter() - t0) / repeats

    t0 = time.perf_counter()
    for _ in range(repeats):
        simple_moving_average_deque(data, window)
    t_deque = (time.perf_counter() - t0) / repeats

    return {"list": t_list, "deque": t_deque}
