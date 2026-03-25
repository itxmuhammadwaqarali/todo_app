from pydantic import BaseModel
from typing import Optional

class TodoCreate(BaseModel):
    title: str
    task: str

class TodoOut(BaseModel):
    id: int
    title: str
    task: Optional[str]

    class Config:
        from_attributes = True
