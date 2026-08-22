from fastapi import APIRouter, UploadFile, File
from services.memory_service import save_memory

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    return await save_memory(file)