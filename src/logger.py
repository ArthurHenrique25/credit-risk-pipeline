import logging
import os

def setup_logger():
    # garante que a pasta logs existe
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        filename="logs/pipeline.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logger = logging.getLogger()
    return logger