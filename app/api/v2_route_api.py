from fastapi import APIRouter, Depends
from app.database.db_connection import get_Db
from app.services.note_service import ProcessNoteService

router = APIRouter(prefix="/api/v2/notes", tags=["Notes v2"])

@router.get("/by-tag/{tag}")
async def get_by_tag(tag: str, db=Depends(get_Db)):
    service = ProcessNoteService(db)
    notes = await service.collection.find({
        "tags": tag,
        "deleted": False
    }).to_list(None)

    return [{"id": str(n["_id"]), **n} for n in notes]
