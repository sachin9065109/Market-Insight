import logging
import sys
from datetime import datetime
from pathlib import Path

_LOG_FORMAT = "[%(asctime)s]: %(name)s: %(levelname)s: %(lineno)d: %(message)s"
_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def _configure_root_logger() -> None:
    root_logger = logging.getLogger()
    
    if root_logger.hasHandlers():
        return

    current_time = datetime.now()
    log_dir = Path("logs") / current_time.strftime("%Y-%m-%d")
    log_dir.mkdir(parents=True, exist_ok=True)
    
    log_file = log_dir / f"{current_time.strftime('%Y-%m-%d_%H-%M-%S')}.log"

    formatter = logging.Formatter(fmt=_LOG_FORMAT, datefmt=_DATE_FORMAT)

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(formatter)

    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)


_configure_root_logger()


def get_logger(name: str) -> logging.Logger:
    """
    Retrieves a configured logger instance for the specified module.
    """
    return logging.getLogger(name)
