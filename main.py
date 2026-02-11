from fastapi import FastAPI
from pydantic import BaseModel
from agent import ask

app = FastAPI(title='ai')

class Prompt(BaseModel):
    prompt: str

@app.post("/compl")
async def compl(data: Prompt):
    result = await ask(data)
    return {'answer': result}

