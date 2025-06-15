import time
import yaml
import state
from logger import get_logger

logger = get_logger(__name__)

def load_services() -> dict | None:
    try:
        with open(state.services_file_path, 'r') as stream:
            data = yaml.safe_load(stream)
            logger.info("Services loaded successfully.")
            return data
    except Exception as e:
        logger.error(f"Error loading services: {e}")
        return None

def refresh_services_periodically(interval_seconds: int = 3600) -> None:
    while True:
        state.services_data = load_services()
        time.sleep(interval_seconds)