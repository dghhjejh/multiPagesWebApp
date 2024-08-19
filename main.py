from typing import Union
from typing import Optional
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import datetime
from bson.objectid import ObjectId
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware
import uuid

app = FastAPI()
# MongoDB connection
client = MongoClient("mongodb+srv://emma:weJ9rynf0qLDcvuh@fistmultipagessiteclust.dg0jk.mongodb.net/?retryWrites=true&w=majority&appName=FistMultipagesSiteCluster")
db = client.to_do_list_app_database
collection = db.thing_to_do

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Taches(BaseModel):
    id: str|None=None
    titre: str
    date: datetime.date
    description: str|None = None

allTasks: list[Taches] = []
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/Taches", response_model=List[Taches])
async def read_task():
    allTasks = list(collection.find())
    for task in allTasks:
        task["_id"] = str(task["_id"])
        task["id"] = str(task["_id"])
    return allTasks

@app.post("/Taches", response_model=Taches)
async def create_tache(task: dict):
    result = collection.insert_one(task)
    if not result.acknowledged:
        raise HTTPException(status_code=500, detail="Could not create task")
    return task

@app.delete("/Taches/{indice}", response_model=dict)
async def delete_task(indice: str):
    try:
        to_delete_object_id = ObjectId(indice)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid task ID")

    result = collection.delete_one({"_id": to_delete_object_id})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"detail": "Task deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)