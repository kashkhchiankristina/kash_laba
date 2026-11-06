"""
Валидация пользовательского ввода для расчёта насоса.
- Проверка границ через if-elif-else.
- Циклический ввод до корректного значения.
"""

from __future__ import annotations

from connstans import Q_MIN, Q_MAX, H_MIN, H_MAX, RHO_MIN, RHO_MAX
from logger import log_error


def validate_range(value: float, low: float, high: float) -> tuple[bool, str]:
    """
    Проверка попадания value в [low, high] через if-elif-else.
    :return: (True, "") или (False, сообщение)
    """
    if value < low:
        return False, f"Ошибка: значение меньше нижней границы ({low})."
    elif value > high:
        return False, f"Ошибка: значение больше верхней границы ({high})."
    else:
        return True, ""


def input_number(prompt: str, low: float, high: float) -> float:
    """
    Циклически запрашивать число, пока не будет корректного.
    Проверяет тип (float) через try/except ValueError и границы.
    """
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError as e:
            msg = str(e.args[0]) if e.args else str(e)
            msg = f"Ошибка: введено не число ('{raw}'). {msg}"
            print(msg)
            log_error(msg)
            continue

        ok, msg = validate_range(value, low, high)
        if ok:
            return value
        print(msg + " Повторите ввод.")
        log_error(msg)


def input_flow() -> float:
    """Циклический ввод подачи Q, м³/ч (0.5..500)."""
    return input_number(
        "Введите подачу Q, м³/ч (допустимо 0.5–500): ",
        Q_MIN, Q_MAX,
    )


def input_head() -> float:
    """Циклический ввод напора H, м (1..200)."""
    return input_number(
        "Введите напор H, м (допустимо 1–200): ",
        H_MIN, H_MAX,
    )


def input_density() -> float:
    """Циклический ввод плотности среды ρ, кг/м³ (800–1200)."""
    return input_number(
        "Введите плотность среды ρ, кг/м³ (допустимо 800–1200): ",
        RHO_MIN, RHO_MAX,
    )
