from fastapi import FastAPI
from .database import Base, engine
from .routers import auth, tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI CRUD + JWT")
app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"status": "ok"}

