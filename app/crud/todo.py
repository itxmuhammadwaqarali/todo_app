from sqlalchemy.orm import Session
from app.models.todo import Todo

def create_todo(db: Session, title: str, task: str, user_id: int):
    todo = Todo(title=title, task=task, owner_id=user_id)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def get_todos(db: Session, user_id: int):
    return db.query(Todo).filter(Todo.owner_id == user_id).all()
