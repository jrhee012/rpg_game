import logging
# import sys

log_level: dict = {
    "CRITICAL": 50,
    "FATAL": 50,
    "ERROR": 40,
    "WARNING": 30,
    "WARN": 30,
    "INFO": 20,
    "DEBUG": 10,
    "NOTSET": 0
}


class Logger:

    def __init__(self, name: str = "MAIN", level: str = "DEBUG"):
        logger = logging.getLogger(name)
        log_lvl = self.get_log_level(level)
        logger.setLevel(log_lvl)

        ch = logging.StreamHandler()
        ch.setLevel(log_lvl)

        logger.addHandler(ch)

    @staticmethod
    def get_log_level(level: str = "DEBUG") -> str:
        log_lvl: str
        for key in log_level:
            if key == level:
                log_lvl = log_level[key]
                break

        if log_lvl is None:
            log_lvl = 0

        return log_lvl

    def update_logger_level(self, name: str = "MAIN", level: str = "DEBUG") -> None:
        logger = logging.getLogger(name)
        log_lvl: str = self.get_log_level(level=level)
        logger.setLevel(log_lvl)

    def update_stream_level(self, name: str = "MAIN", level: str = "DEBUG") -> None:
        logger = logging.getLogger(name)
        log_lvl: str = self.get_log_level(level=level)
        ch = logging.StreamHandler()
        ch.setLevel(log_lvl)
        logger.addHandler(ch)
