"""
logging.py
"""
import logging


def start_log(log_level):
    if log_level == "DEBUG":
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler(filename="troload.log"),
            ],
        )
    else:
        if log_level == "INFO":
            logging.basicConfig(
                level=logging.INFO,
                format="%(asctime)s %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
                handlers=[
                    logging.StreamHandler(),
                    logging.FileHandler(filename="troload.log"),
                ],
            )
    return logging
