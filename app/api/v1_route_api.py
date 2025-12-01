from fastapi import APIRouter,Depends,HTTPException
from bson import ObjectId

from app.database.db_connection import get_Db
from app.services.note_service import ProcessNoteService
from app.utils.model_schema import NoteBase, NoteOut
from app.utils.logging import write_audit

router = APIRouter(prefix='/api/v1/notes',tags=['Notes'])

def get_service(db=Depends(get_Db)):
    return ProcessNoteService(db), db

@router.post("/", response_model=NoteOut)
async def create_note(note: NoteBase, deps=Depends(get_service)):
    if not note.title:
        raise HTTPException(400, "Title is required")

    process, db = deps
    doc = await process.create(note.dict())
    await write_audit(db, "create", str(doc["_id"]))

    return {"id": str(doc["_id"]), **doc}

@router.get("/{id}", response_model=NoteOut)
async def get_note(id: str, deps=Depends(get_service)):
    if not ObjectId.is_valid(id):
        raise HTTPException(400, "Invalid ID")

    service, _ = deps
    doc = await service.get(id)

    if not doc:
        raise HTTPException(404, "Not found")

    return {"id": str(doc["_id"]), **doc}


@router.get("/", response_model=list[NoteOut])
async def list_notes(deps=Depends(get_service)):
    service, _ = deps
    notes = await service.list()

    return [{"id": str(n["_id"]), **n} for n in notes]


@router.put("/{id}", response_model=NoteOut)
async def update_note(id: str, note: NoteBase, deps=Depends(get_service)):
    if not ObjectId.is_valid(id):
        raise HTTPException(400, "Invalid ID")

    service, db = deps
    doc = await service.update(id, note.dict(exclude_unset=True))

    if not doc:
        raise HTTPException(404, "Not found")

    await write_audit(db, "update", id)

    return {"id": str(doc["_id"]), **doc}


@router.delete("/{id}")
async def delete_note(id: str, deps=Depends(get_service)):
    if not ObjectId.is_valid(id):
        raise HTTPException(400, "Invalid ID")

    service, db = deps
    await service.soft_delete(id)
    await write_audit(db, "delete", id)

    return {"message": "Soft deleted successfully"}