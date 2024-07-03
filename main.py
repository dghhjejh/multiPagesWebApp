from typing import Union
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import datetime
from fastapi.middleware.cors import CORSMiddleware

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
    allow_methods=["POST", "OPTIONS", "DELETE", "PUT"],
    allow_headers=["*"],
)

class Taches(BaseModel):
    titre: str
    date: datetime.date
    description: str|None = None
allTasks = [{"titre":"achat", "date": "2024-06-24", "description": "je vais faire les achats bientôt"},
            {"titre":"dormir", "date": "2024-06-24", "description": "c'est ferié et je vais dormir"},
            {"titre":"manger", "date": "2024-06-13", "description": "je mange très mal"}]
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/Taches")
def read_tache():
    return allTasks

@app.put("/Taches")
def update_tache(tache : Taches):
    for task in allTasks:
        if task["titre"] == tache.titre:
            task["date"] = tache.date
            task["description"] = tache.description
            return "task updated smoothly"
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/Taches")
def create_tache(tache : Taches):
    allTasks.append(tache)
    return tache

@app.delete("/Taches/{indice}")
def delete_tache(indice: int):
    for  indiceTache, task in enumerate(allTasks):
        if indiceTache == indice:
            allTasks.remove(task)
            return " task removed correctly"
    raise HTTPException(status_code=404, detail= "Task not found")



