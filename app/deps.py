from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from .auth import get_current_user
from .database import get_db
from .models import Task

def get_owned_task(task_id: int, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id, Task.owner_id == current_user.id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task

