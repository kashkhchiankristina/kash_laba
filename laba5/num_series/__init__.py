from .generator import uniform_series
from .stats import mean, median, spread, variance, stdev, summarize
from .moving_average import (
    simple_moving_average,
    exponential_moving_average,
    benchmark_moving_average,
)
from .deque_average import (
    simple_moving_average_deque,
    centered_moving_average_deque,
    exponential_moving_average_deque,
)
from .io_json import save_series_json, load_series_json
from .io_file import load_series_txt, load_series_csv, load_series_auto

__all__ = [
    "uniform_series",
    "mean",
    "median",
    "spread",
    "variance",
    "stdev",
    "summarize",
    "simple_moving_average",
    "exponential_moving_average",
    "benchmark_moving_average",
    "simple_moving_average_deque",
    "centered_moving_average_deque",
    "exponential_moving_average_deque",
    "save_series_json",
    "load_series_json",
    "load_series_txt",
    "load_series_csv",
    "load_series_auto",
]
