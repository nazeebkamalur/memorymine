from fastapi import APIRouter
from pydantic import BaseModel

from services.vector_service import search_vectors
from services.llm_service import generate_answer

router = APIRouter()

class ChatRequest(BaseModel):
    question: str

@router.post("/chat")
async def chat(req: ChatRequest):
    memories = search_vectors(req.question)

    if not memories:
        return {
            "answer": "No relevant memory found.",
            "results": []
        }

    best_memory = [memories[0]]

    answer = generate_answer(req.question, best_memory)

    return {
        "answer": answer,
        "results": best_memory
    }