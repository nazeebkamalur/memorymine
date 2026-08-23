from PIL import Image
import pytesseract
import pymupdf as fitz

# Windows Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(file_path):
    # PDF
    if file_path.lower().endswith(".pdf"):
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text.strip()

    # Image (PNG/JPG/JPEG)
    img = Image.open(file_path)
    return pytesseract.image_to_string(img).strip()