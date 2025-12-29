from fastapi import FastAPI
from backend.demo.pipeline import run_demo_pipeline
from backend.xray.store import get_execution, get_all_executions
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/run-demo")
def run_demo():
    execution_id = run_demo_pipeline()
    return {"execution_id": execution_id}

@app.get("/execution/{execution_id}")
def get_execution_data(execution_id: str):
    execution = get_execution(execution_id)
    if not execution:
        return {"error": "Execution not found"}
    return execution.to_dict()

@app.get("/executions")
def list_executions():
    return {
        k: v.to_dict()
        for k, v in get_all_executions().items()
    }
