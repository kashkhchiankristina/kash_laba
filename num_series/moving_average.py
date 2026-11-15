"""Скользящие средние: SMA, центрированное MA, EMA.

SMA реализована через бегущую сумму — O(n) вместо O(n * w).
"""

from typing import List, Sequence


def check_window(window: int, n: int) -> None:
    """Валидация окна: целое >= 1 и не больше длины ряда."""
    try:
        is_positive_int = (window >= 1) and (int(window) == window)
    except (TypeError, ValueError) as err:
        raise ValueError(
            f"window должно быть целым числом >= 1 "
            f"(получено: {window!r}; причина: {err.args[0]})"
        ) from err
    if not is_positive_int:
        raise ValueError(f"window должно быть целым числом >= 1 (получено: {window!r})")
    if window > n:
        raise ValueError(
            f"window больше длины ряда (window={window}, n={n})"
        )


def simple_moving_average(data: Sequence[float], window: int) -> List[float]:
    """SMA: среднее по последним window точкам.

    Длина результата: len(data) - window + 1.
    """
    if not data:
        raise ValueError("Ряд пуст: расчёт скользящей средней невозможен")
    check_window(window, len(data))

    running = sum(data[:window])
    result = [running / window]
    for i in range(window, len(data)):
        running += data[i] - data[i - window]
        result.append(running / window)
    return result


def centered_moving_average(data: Sequence[float], window: int) -> List[float]:
    """Центрированное МА: окно нечётное, выход выровнен по центру окна.

    Длина результата: len(data) - window + 1 (края ряда не заполняются).
    """
    if not data:
        raise ValueError("Ряд пуст: расчёт скользящей средней невозможен")
    check_window(window, len(data))
    if window % 2 == 0:
        raise ValueError(
            f"окно центрированного МА должно быть нечётным (получено: {window})"
        )

    half = window // 2
    return [
        sum(data[i - half:i - half + window]) / window
        for i in range(half, len(data) - half)
    ]


def exponential_moving_average(data: Sequence[float], alpha: float) -> List[float]:
    """EMA: EMA[0] = data[0]; EMA[i] = alpha * data[i] + (1 - alpha) * EMA[i - 1].

    Требование: 0 < alpha <= 1. Длина результата равна длине ряда.
    """
    if not data:
        raise ValueError("Ряд пуст: расчёт скользящей средней невозможен")
    try:
        ok = (0.0 < float(alpha) <= 1.0) and (float(alpha) == alpha)
    except (TypeError, ValueError) as err:
        raise ValueError(
            f"alpha должно быть числом в диапазоне 0 < alpha <= 1 "
            f"(получено: {alpha!r}; причина: {err.args[0]})"
        ) from err
    if not ok:
        raise ValueError(
            f"alpha должно быть числом в диапазоне 0 < alpha <= 1 (получено: {alpha!r})"
        )

    result: List[float] = [float(data[0])]
    a = float(alpha)
    for i in range(1, len(data)):
        result.append(a * data[i] + (1.0 - a) * result[-1])
    return result
