from fastapi import FastAPI
import threading
import state
from fastapi import HTTPException
from contextlib import asynccontextmanager
from read_services import refresh_services_periodically
from logger import get_logger

logger = get_logger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    thread = threading.Thread(target=refresh_services_periodically, daemon=True)
    thread.start()
    
    yield  # lifespan pause — app runs here until shutdown

    # shutdown (optional cleanup)
    # thread.join()  # not needed if daemon=True

app = FastAPI(lifespan=lifespan)

@app.get("/ping")
async def ping():
    logger.info("* Ping received *")
    return {"status": "OK"}

@app.get("/services")
async def get_services():
    if not state.services_data:
        logger.error("Services data not loaded")
        raise HTTPException(status_code=404, detail="Services data not loaded")
    logger.info("Sending services...")
    return state.services_data