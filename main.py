from validation import input_flow, input_head, input_density
from menu import show_menu, select_mode, mode_name
from operations import pump_power, head_class


def main() -> None:
    """Главный сценарий."""
    print("=== Расчёт напора и мощности насоса ===")

    while True:
        show_menu()
        eta = select_mode()
        if eta is None:
            print("Работа завершена.")
            break

        q = input_flow()
        h = input_head()
        rho = input_density()

        p = pump_power(q, h, rho, eta)
        cls = head_class(h)

        print("\n Результаты ")
        print(f"Тип насоса:  {mode_name(eta)} (η = {eta})")
        print(f"P (мощность): {p:.2f} кВт")
        print(f"Класс напора: {cls}")
        print("\n")


if __name__ == "__main__":
    main()
