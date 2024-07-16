from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from starlette.responses import RedirectResponse
from motor.motor_asyncio import AsyncIOMotorClient
import uvicorn

app = FastAPI(
    title = settings.APP_NAME,
    version = settings.VERSION
)

async def get_database():
    client = AsyncIOMotorClient(settings.DB_URI)
    try:
        db = client[settings.DB_NAME]
        yield db
    finally:
        client.close()

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
