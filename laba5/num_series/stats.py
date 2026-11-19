from __future__ import annotations

import math
from typing import Dict, Sequence


def _ensure_not_empty(data: Sequence[float]) -> None:
    if not data:
        raise ValueError("Ряд пуст: расчёт статистики невозможен")


def mean(data: Sequence[float]) -> float:
    """Среднее арифметическое."""
    _ensure_not_empty(data)
    return sum(data) / len(data)


def median(data: Sequence[float]) -> float:
    """Медиана ряда."""
    _ensure_not_empty(data)
    s = sorted(data)
    k = len(s) // 2
    if len(s) % 2:
        return float(s[k])
    return (s[k - 1] + s[k]) / 2.0


def spread(data: Sequence[float]) -> float:
    """Размах ряда: max - min."""
    _ensure_not_empty(data)
    return float(max(data) - min(data))


def variance(data: Sequence[float]) -> float:
    """Выборочная дисперсия (знаменатель n - 1)."""
    _ensure_not_empty(data)
    n = len(data)
    if n < 2:
        raise ValueError("Для расчёта выборочной дисперсии требуется минимум 2 элемента")
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / (n - 1)


def stdev(data: Sequence[float]) -> float:
    """Выборочное среднее квадратическое отклонение (СКО)."""
    return math.sqrt(variance(data))


def summarize(data: Sequence[float]) -> Dict[str, float]:
    """Сводный отчёт по всем статистическим показателям."""
    _ensure_not_empty(data)
    return {
        "count": float(len(data)),
        "mean": mean(data),
        "median": median(data),
        "spread": spread(data),
        "min": float(min(data)),
        "max": float(max(data)),
        "variance": variance(data),
        "stdev": stdev(data),
    }
