from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

client = AsyncIOMotorClient(settings.db_urls)

async def get_Db():
    return client[settings.db_db]