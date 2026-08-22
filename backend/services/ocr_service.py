import os
import fitz  # PyMuPDF
import pytesseract
from PIL import Image

def extract_text(path):
    ext = os.path.splitext(path)[1].lower()

    # PDF
    if ext == ".pdf":
        text = ""
        doc = fitz.open(path)
        for page in doc:
            text += page.get_text()
        return text.strip()

    # Images
    elif ext in [".jpg", ".jpeg", ".png"]:
        img = Image.open(path)
        return pytesseract.image_to_string(img).strip()

    # TXT / WhatsApp
    elif ext == ".txt":
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()

    return ""