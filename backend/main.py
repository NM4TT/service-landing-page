import sys
import yaml
from dotenv import load_dotenv
import os
from logger import get_logger

load_dotenv() #for local testing

logger = get_logger(__name__)

services_file_path: str | None = None

def init() -> None:
    global services_file_path
    services_file_path = os.getenv("SERVICES_FILE_PATH") #absolute path
    if not services_file_path:
        logger.error("services_file_path environment variable is empty.")
        sys.exit(1)

def load_services() -> dict:
    try:
        with open(services_file_path, 'r') as stream:
            services_data = yaml.safe_load(stream)
            logger.info("Services loaded successfully.")
            return services_data
    except FileNotFoundError:
        logger.error(f"File not found: {services_file_path}")
        sys.exit(1)
    except yaml.YAMLError as exc:
        logger.error(f"Error parsing YAML: {exc}")
        sys.exit(1)
    except Exception as exc:
        logger.error(f"Unexpected error: {exc}")
        sys.exit(1)

def main() -> None:
    init()
    services = load_services()
    print(services)

if __name__ == "__main__":
    main()