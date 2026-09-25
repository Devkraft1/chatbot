from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from search import search
from promptGen import generateprompt
from userResponse import generateUserResponse
app = FastAPI()

origins = [
    "https://test.zsp3zamosc.pl/",
    "https://zsp3zamosc.pl/",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Query(BaseModel):
    query: str
@app.post("/query")
def root(query: Query):
    q = query.query[:100]
    context = search(q)
    prompt = generateprompt(q, context)
    answer = generateUserResponse(prompt)
    return {
        "answer": answer
    }