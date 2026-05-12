import logging
import os

os.makedirs("logs", exist_ok=True)

def get_logger(nom):
    logger = logging.getLogger(nom)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # Console
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

        # Fichier
        fichier = logging.FileHandler("logs/tests.log", encoding="utf-8")
        fichier.setFormatter(formatter)
        logger.addHandler(fichier)

    return logger