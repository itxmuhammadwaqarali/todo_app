from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.schemas.todo import TodoCreate, TodoOut, TodoUpdate
from app.crud import user as crud_user
from app.crud import todo as crud_todo
from app.core.auth import create_access_token
from app.api.dependencies import get_db, get_current_user
import uuid

router = APIRouter()


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return crud_user.create_user(db, user.username, user.password)


@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.authenticate(db, user.username, user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token({"user_id": db_user.id})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/todos", response_model=TodoOut)
def create(todo: TodoCreate,
           db: Session = Depends(get_db),
           current_user=Depends(get_current_user)):
    return crud_todo.create_todo(db, todo.title, todo.task, current_user.id)


@router.get("/todos", response_model=list[TodoOut])
def read(db: Session = Depends(get_db),
         current_user=Depends(get_current_user)):
    return crud_todo.get_todos(db, current_user.id)


@router.patch("/todos/{todo_id}", response_model=TodoOut)
def update_todo_api(todo_id: str, updates: TodoUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    todo_uuid = uuid.UUID(todo_id)
    updated = crud_todo.update_todo(db, todo_uuid, current_user.id, updates.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated


@router.delete("/todos/{todo_id}")
def delete_todo_api(todo_id: str, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    todo_uuid = uuid.UUID(todo_id)
    deleted = crud_todo.delete_todo(db, todo_uuid, current_user.id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"ok": True}
