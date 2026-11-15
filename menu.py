"""
Меню выбора типа насоса через match-case.
"""

from __future__ import annotations

from connstans import ETA_CENTRIFUGAL, ETA_PISTON, ETA_VORTEX


def show_menu() -> None:
    """Вывести меню насосов."""
    print("\n Выберите тип насоса:")
    print("  1 — центробежный (η = 0.75)")
    print("  2 — поршневой    (η = 0.85)")
    print("  3 — вихревой     (η = 0.55)")
    print("  0 — выход")


def select_mode() -> float | None:
    """
    Циклически запрашивать тип насоса и возвращать КПД η.

    Использует match-case для маршрутизации.
    Возвращает None, если выбран выход (0).
    """
    while True:
        choice = input("Введите номер насоса (от 0 до 3): ").strip()
        match choice:
            case "1":
                return ETA_CENTRIFUGAL
            case "2":
                return ETA_PISTON
            case "3":
                return ETA_VORTEX
            case "0":
                return None
            case _:
                print("Ошибка: неверный пункт меню. Повторите ввод.")


def mode_name(eta: float) -> str:
    """Вернуть название типа насоса по КПД η."""
    match eta:
        case 0.75:
            return "центробежный"
        case 0.85:
            return "поршневой"
        case 0.55:
            return "вихревой"
        case _:
            return "неизвестный"
