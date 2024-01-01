import json
import os
import subprocess
from datetime import datetime
from functools import wraps
from typing import Union


def subprocess_error_handler(func):  # type: ignore
    @wraps(func)
    def wrapper(*args, **kwargs):  # type: ignore
        try:
            func(*args, **kwargs)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while executing command: [{e}]")

        except FileNotFoundError as e:
            print(f"Command not found: {e}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return None

    return wrapper


def get_now_time_hms() -> str:
    current = datetime.now()
    hms_time = current.strftime("%H:%M:%S")
    return hms_time


class LogWriter:
    def __init__(self, log_dir: str = "logs") -> None:
        self.log_dir = log_dir
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
        self.log_file = os.path.join(
            log_dir, f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )

    def add_scalar(
        self, x_value: Union[int, float], y_value: Union[int, float]
    ) -> None:
        data = {"tag": "xy", "x_value": x_value, "y_value": y_value}
        with open(self.log_file, "a") as f:
            f.write(json.dumps(data) + "\n")

    @subprocess_error_handler
    def add_gpu_status(self) -> None:
        query = "utilization.gpu"
        output_fmt = "csv,nounits,noheader"
        cmd = f"nvidia-smi --query-gpu={query} --format={output_fmt}"
        result = subprocess.run(
            cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
        )
        gpu_utilization = int(result.stdout.decode("utf-8").strip())
        hms_time = get_now_time_hms()
        data = {"tag": "gpu", "utilz_gpu": gpu_utilization, "hms_time": hms_time}
        with open(self.log_file, "a") as f:
            f.write(json.dumps(data) + "\n")
