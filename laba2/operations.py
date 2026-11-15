"""
Расчёты: мощность насоса P, класс напора.
"""

from typing import Annotated

from connstans import G, H_LOW_LIMIT, H_HIGH_LIMIT


def pump_power(
    q: Annotated[float, "Подача, м3/ч"],
    h: Annotated[float, "Напор, м"],
    rho: Annotated[float, "Плотность среды, кг/м3"],
    eta: Annotated[float, "КПД насоса"],
) -> float:
    """
    Рассчитать мощность насоса
    P = rho · g · Q · H / (3600 · eta · 1000), кВт.

    Args:
        q: подача, м3/ч.
        h: напор, м.
        rho: плотность среды, кг/м3.
        eta: КПД насоса.

    Returns:
        Мощность, кВт.
    """
    return rho * G * q * h / (3600.0 * eta * 1000.0)


def head_class(
    h: Annotated[float, "Напор, м"],
) -> str:
    """
    Классифицировать напор через if-elif-else.

    H < 10 — малый напор;
    10 ≤ H ≤ 60 — средний напор;
    H > 60 — высокий напор.

    Args:
        h: напор, м.

    Returns:
        Строка с названием класса напора.
    """
    if h < H_LOW_LIMIT:
        return "малый напор"
    elif h <= H_HIGH_LIMIT:
        return "средний напор"
    else:
        return "высокий напор"
