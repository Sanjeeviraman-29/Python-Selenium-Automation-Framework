import logging
import os


class Logger:

    @staticmethod
    def get_logger():

        os.makedirs("logs", exist_ok=True)

        logger = logging.getLogger("AutomationFramework")

        # Configure only once
        if not logger.handlers:

            logger.setLevel(logging.INFO)

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )

            file_handler = logging.FileHandler(
                "logs/automation.log",
                mode="a",
                encoding="utf-8"
            )

            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

        return logger