import math

# --- КПД насосов (Вариант 11) ---
ETA_CENTRIFUGAL: float = 0.75   # центробежный
ETA_PISTON: float = 0.85        # поршневой
ETA_VORTEX: float = 0.55        # вихревой

# --- Допустимые диапазоны входных данных ---
Q_MIN: float = 0.5              # подача, м3/ч
Q_MAX: float = 500.0
H_MIN: float = 1.0              # напор, м
H_MAX: float = 200.0
RHO_MIN: float = 800.0          # плотность среды, кг/м3
RHO_MAX: float = 1200.0

# --- Пороговые значения для классификации напора ---
H_LOW_LIMIT: float = 10.0       # H < 10  — малый напор
H_HIGH_LIMIT: float = 60.0      # 10..60 — средний; H > 60 — высокий

# --- Физическая константа ---
G: float = 9.81                 # ускорение свободного падения, м/с2

# --- Файл журнала ошибок ---
LOG_FILE: str = "input_errors.log"
