from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.models.todo import Todo, PriorityEnum
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
    return crud_todo.create_todo(
        db,
        todo.title,
        todo.task,
        current_user.id,
        todo.priority,
        todo.due_date
    )


@router.get("/todos", response_model=list[TodoOut])
def read(db: Session = Depends(get_db),
         current_user=Depends(get_current_user)):
    todos = crud_todo.get_todos(db, current_user.id)

    if not todos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No todos found."
        )
    return todos


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


@router.patch("/todos/{todo_id}/toggle", response_model=TodoOut)
def toggle_todo_api(
    todo_id: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    try:
        todo_uuid = uuid.UUID(todo_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid todo id")

    updated = crud_todo.toggle_todo(db, todo_uuid, current_user.id)

    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")

    return updated

@router.get("/todos/search", response_model=list[TodoOut])
def search_todos(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
    q: Optional[str] = Query(None, description="Search term in title or task"),
    priority: Optional[PriorityEnum] = None,
    completed: Optional[bool] = None
):
    query = db.query(Todo).filter(Todo.owner_id == current_user.id)

    if q:
        query = query.filter(
            (Todo.title.ilike(f"%{q}%")) |
            (Todo.task.ilike(f"%{q}%"))
        )
    if priority:
        query = query.filter(Todo.priority == priority)
    if completed is not None:
        query = query.filter(Todo.completed == completed)

    return query.all()

@router.get("/todos/stats")
def todos_stats(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    total = db.query(Todo).filter(Todo.owner_id == current_user.id).count()
    completed = db.query(Todo).filter(Todo.owner_id == current_user.id, Todo.completed == True).count()
    pending = total - completed
    return {"total": total, "completed": completed, "pending": pending}