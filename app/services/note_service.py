from datetime import datetime
from bson import ObjectId

class ProcessNoteService:
    def __init__(self,db):
        self.collection=db.notes

    async def create_notes(self,data):
        now = datetime.now()
        doc = {
            **data,
            "created_at": now,
            "updated_at": now,
            "deleted": False
        }
        result = await self.collection.insert_one(doc)
        doc["_id"] = result.inserted_id
        return 
    
    async def get_notes(self, id):
        return await self.collection.find_one({
            "_id": ObjectId(id),
            "deleted": False
        })
    


    async def list_notes(self):
        return await self.collection.find({"deleted": False}).to_list(None)
    

    async def update(self, id, data):
        return await self.collection.find_one_and_update(
            {"_id": ObjectId(id), "deleted": False},
            {"$set": {**data, "updated_at": datetime.now()}},
            return_document=True
        )

    async def soft_delete(self, id):
        return await self.collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": {"deleted": True, "updated_at": datetime.now()}}
        )

