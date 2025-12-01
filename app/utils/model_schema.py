from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# for BOTH create ,update
class NoteBase(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    tags: Optional[List[str]] = []

# for API response
class NoteOut(BaseModel):
    id: str
    title: str
    content: Optional[str]
    tags: List[str]
    created_at: datetime
    updated_at: datetime
