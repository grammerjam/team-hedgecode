from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from motor.motor_asyncio import AsyncIOMotorClient
import uvicorn # NOTE: used in main

from config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connect to MongoDB before serving requests
    app.mongodb_client = AsyncIOMotorClient(settings.DB_URI)
    app.mongodb = app.mongodb_client[settings.DB_NAME]
    yield

    # Close MongoDB connection after serving requests
    app.mongodb_client.close()

async def get_database():
    try:
        return app.mongodb
    except RuntimeError as e:
        raise RuntimeError(f"Database client not initialized: {e}")
    except Exception as e:
        raise Exception(f"Error during database initiation: {e}")

app = FastAPI(
    title = settings.APP_NAME,
    version = settings.VERSION,
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

# Redirect / -> Swagger-UI documentation
@app.get("/")
async def main_function():
    """
    # Redirect
    to documentation (`/docs/`).
    """
    return RedirectResponse(url="/docs/")


# if __name__ == "__main__":
#     uvicorn.run(
#         "main:app",
#         host=settings.HOST,
#         reload=settings.DEBUG_MODE,
#         port=settings.PORT,
#     )
