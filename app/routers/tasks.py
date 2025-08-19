from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..auth import get_current_user
from ..database import get_db
from ..deps import get_owned_task

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=schemas.TaskOut, status_code=201)
def create_task(payload: schemas.TaskCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    task = models.Task(**payload.model_dump(), owner_id=current_user.id)
    db.add(task); db.commit(); db.refresh(task)
    return task

@router.get("/", response_model=List[schemas.TaskOut])
def list_tasks(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return db.query(models.Task).filter(models.Task.owner_id == current_user.id).all()

@router.get("/{task_id}", response_model=schemas.TaskOut)
def get_task(task_id: int, task=Depends(get_owned_task)):
    return task

@router.put("/{task_id}", response_model=schemas.TaskOut)
def update_task(task_id: int, payload: schemas.TaskCreate, db: Session = Depends(get_db), task=Depends(get_owned_task)):
    task.title = payload.title; task.description = payload.description
    db.commit(); db.refresh(task); return task

@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db), task=Depends(get_owned_task)):
    db.delete(task); db.commit(); return

