from fastapi import FastAPI,Request
from app.util.log_util import setup_logger
import uvicorn 
from contextlib import asynccontextmanager  # noqa: E402
from app.core.deepface_service import router as deepface_router

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Application startup")
    yield
    # Shutdown
    logger.info("Application shutdown")

    
logger = setup_logger('main')
app = FastAPI(lifespan=lifespan)

@app.middleware("http")
async def log_request(request: Request, call_next):

    response = await call_next(request)
    
    return response

app.include_router(deepface_router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)