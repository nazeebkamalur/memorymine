from fastapi import APIRouter
from services.memory_service import get_all_memories

router = APIRouter()

@router.get("/memories")
def memories():
    return get_all_memories()