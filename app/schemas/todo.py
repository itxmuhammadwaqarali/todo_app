from pydantic import BaseModel
from typing import Optional
import uuid

class TodoCreate(BaseModel):
    title: str
    task: str

class TodoOut(BaseModel):
    id: uuid.UUID
    title: str
    task: Optional[str]

    class Config:
        from_attributes = True

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    task: Optional[str] = None
