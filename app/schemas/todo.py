from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from app.models.todo import PriorityEnum
import uuid

class TodoCreate(BaseModel):
    title: str
    task: Optional[str] = ""
    priority: Optional[PriorityEnum] = PriorityEnum.medium
    due_date: Optional[datetime] = None  # optional due date input

class TodoOut(BaseModel):
    id: uuid.UUID
    title: str
    task: Optional[str]
    completed: bool
    priority: PriorityEnum
    created_at: datetime
    due_date: Optional[datetime]

    class Config:
        from_attributes = True

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    task: Optional[str] = None
    completed: Optional[bool] = None
    priority: Optional[PriorityEnum] = None
    due_date: Optional[datetime] = None
