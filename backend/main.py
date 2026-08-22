from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.upload import router as upload_router
from routes.memories import router as memories_router
from routes.search import router as search_router
from routes.chat import router as chat_router

app = FastAPI(title="MemoryMine AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(memories_router)
app.include_router(search_router)
app.include_router(chat_router)

@app.get("/")
def root():
    return {"message": "MemoryMine API Running"}