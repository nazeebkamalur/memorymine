from pydantic import BaseModel
from typing import Optional, Dict

class Memory(BaseModel):
    id: str
    source_type: str
    filename: str
    text: str
    sender: Optional[str] = None
    timestamp: Optional[str] = None
    file_path: str
    metadata: Dict = {}