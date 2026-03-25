from sqlalchemy.orm import Session
from app.models.todo import Todo
import uuid

def create_todo(db: Session, title: str, task: str, user_id: int):
    todo = Todo(title=title, task=task, owner_id=user_id)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def get_todos(db: Session, user_id: int):
    return db.query(Todo).filter(Todo.owner_id == user_id).all()

def update_todo(db: Session, todo_id: uuid.UUID, user_id: uuid.UUID, updates: dict):
    todo = db.query(Todo).filter(Todo.id == todo_id, Todo.owner_id == user_id).first()
    if not todo:
        return None
    for key, value in updates.items():
        if hasattr(todo, key) and value is not None:
            setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo

def delete_todo(db: Session, todo_id: uuid.UUID, user_id: uuid.UUID):
    todo = db.query(Todo).filter(Todo.id == todo_id, Todo.owner_id == user_id).first()
    if not todo:
        return False
    db.delete(todo)
    db.commit()
    return True
