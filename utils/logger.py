import logging
import os
from datetime import datetime

def setup_logger(log_dir="logs", log_file="app.log", log_level=logging.INFO):
    """
    Configures the logger to write to a file and console.

    Args:
        log_dir (str): Directory where the log file will be stored.
        log_file (str): Name of the log file.
        log_level (int): Logging level (e.g., logging.INFO, logging.DEBUG).

    Returns:
        logging.Logger: Configured logger instance.
    """
    # Ensure the log directory exists
    os.makedirs(log_dir, exist_ok=True)

    # Configure log file path
    log_path = os.path.join(log_dir, log_file)

    # Create and configure logger
    logger = logging.getLogger("AppLogger")
    logger.setLevel(log_level)

    # Prevent duplicate handlers
    if not logger.handlers:
        # File handler for logging to a file
        file_handler = logging.FileHandler(log_path)
        file_handler.setLevel(log_level)

        # Console handler for logging to the terminal
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)

        # Formatter for logs
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger


def log_info(logger, message):
    """
    Logs an informational message.

    Args:
        logger (logging.Logger): Logger instance.
        message (str): Message to log.
    """
    logger.info(message)


def log_error(logger, message):
    """
    Logs an error message.

    Args:
        logger (logging.Logger): Logger instance.
        message (str): Message to log.
    """
    logger.error(message)


def log_debug(logger, message):
    """
    Logs a debug message.

    Args:
        logger (logging.Logger): Logger instance.
        message (str): Message to log.
    """
    logger.debug(message)


def log_exception(logger, message):
    """
    Logs an exception with traceback.

    Args:
        logger (logging.Logger): Logger instance.
        message (str): Message to log.
    """
    logger.exception(message)
