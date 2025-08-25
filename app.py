from fastapi import FastAPI
from pydantic import BaseModel
from crew import run_crew

app = FastAPI()

class Query(BaseModel):
    input: str

@app.get("/")
def root():
    return {"message": "🚀 CrewAI est en ligne sur Render"}

@app.post("/run")
def run_agent(query: Query):
    result = run_crew(query.input)
    return {"result": result}
