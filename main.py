from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from search import search
from promptGen import generateprompt
from userResponse import generateUserResponse
app = FastAPI()

origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)

class Query(BaseModel):
    query: str
@app.post("/query")
async def root(query: Query):
    q = query.query[:100]
    context = search(q)
    prompt = generateprompt(q, context)
    return generateUserResponse(prompt)