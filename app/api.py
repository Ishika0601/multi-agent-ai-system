from fastapi import FastAPI
from app.orchestration.workflow import execute

app = FastAPI(title="Multi-Agent AI Research System")

@app.get("/run")
def run(goal: str):
    return execute(goal)
