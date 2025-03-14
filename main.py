from fastapi import FastAPI
from task import Task

app = FastAPI()

tasks = [
    Task(),
    Task()
]

@app.get("/")
def root():
    return "Hello World"

@app.get("/get-tasks")
def get_all_tasks():
    return tasks