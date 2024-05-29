from celery.result import AsyncResult
from fastapi import Body, FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from worker import create_task


app = FastAPI()

class Request(BaseModel):
    task_type: int


@app.post("/tasks", status_code=201)
async def run_task(payload: Request):
    task_type = payload.task_type
    task = create_task.delay(int(task_type))
    return {"task_id": task.id}


@app.get("/tasks/{task_id}")
async def get_status(task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return result
