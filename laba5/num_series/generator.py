from __future__ import annotations

import random
from typing import List, Optional


def _validate_n(n: int) -> None:
    """Проверка, что n — положительное целое число."""
    if isinstance(n, bool):
        raise ValueError(f"n должно быть положительным целым числом (получено: {n!r})")
    try:
        is_positive_int = (n > 0) and (int(n) == n)
    except (TypeError, ValueError) as err:
        raise ValueError(
            f"n должно быть положительным целым числом (получено: {n!r}; причина: {err.args[0]})"
        ) from err

    if not is_positive_int:
        raise ValueError(f"n должно быть положительным целым числом (получено: {n!r})")


def uniform_series(
    n: int = 1000,
    low: float = 0.0,
    high: float = 100.0,
    seed: Optional[int] = None,
) -> List[float]:
    """Ряд из n чисел равномерного распределения на [low, high)."""
    _validate_n(n)
    if low >= high:
        raise ValueError(f"low должно быть меньше high (получено: {low} >= {high})")
    rng = random.Random(seed)
    return [float(rng.uniform(low, high)) for _ in range(n)]
