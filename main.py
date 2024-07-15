from typing import Union
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import datetime
from fastapi.middleware.cors import CORSMiddleware
import uuid
app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Taches(BaseModel):
    id: str
    titre: str
    date: datetime.date
    description: str|None = None

allTasks: list[Taches] = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/Taches", response_model=list[Taches])
def read_tache():
    return allTasks

@app.put("/Taches")
def update_tache(tache : Taches):
    for task in allTasks:
        if task.id == tache.id:
            task.titre = tache.titre
            task["date"] = tache.date
            task["description"] = tache.description
            return "task updated smoothly"
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/Taches", response_model=Taches)
def create_tache(tache: dict):
    new_task = Taches(id=str(uuid.uuid4()), titre=tache["titre"], date=tache["date"], description=tache["description"])
    allTasks.append(new_task)
    return new_task

@app.delete("/Taches/{indice}", response_model=dict)
def delete_tache(indice: str):
    for  task in allTasks:
        if task.id == indice:
            allTasks.remove(task)
            return {"message":"task removed correctly"}
    raise HTTPException(status_code=404, detail= "Task not found")

