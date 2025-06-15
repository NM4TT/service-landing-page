import sys
import uvicorn
import os
import state
from dotenv import load_dotenv
from logger import get_logger
from server import app

load_dotenv() #for local testing

logger = get_logger(__name__)

def init() -> None:
    state.services_file_path = os.getenv("SERVICES_FILE_PATH", "./data/services.yaml") #absolute path
    if not state.services_file_path:
        logger.error("services_file_path environment variable is empty.")
        sys.exit(1)
    server_port_str = os.getenv("SERVER_PORT", "8081")
    try:
        state.server_port = int(server_port_str)
    except ValueError:
        logger.error(f"Invalid port number: {server_port_str}, defaulting to 8081")
        state.server_port = 8081


def main() -> None:
    init()
    
    uvicorn.run(app, host="0.0.0.0", port=state.server_port)

if __name__ == "__main__":
    main()