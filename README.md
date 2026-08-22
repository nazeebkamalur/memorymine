# 🧠 MemoryMine AI — Digital Memory Assistant

MemoryMine AI is a modern AI-powered digital memory assistant that indexes documents, OCR images, PDFs, and WhatsApp chat logs into a dense FAISS vector database for real-time semantic search and conversational AI (RAG).

---

## 🚀 Quick Start Guide

### 1. Start the FastAPI Backend

Open a terminal in the `backend/` directory:

```bash
cd backend
.venv\Scripts\activate      # On Windows (or source .venv/bin/activate on Mac/Linux)
uvicorn main:app --reload --port 8000
```

Backend API will run on `http://127.0.0.1:8000` with Swagger docs at `http://127.0.0.1:8000/docs`.

---

### 2. Start the Modern React Frontend

Open a second terminal in the `frontend/` directory:

```bash
cd frontend
npm run dev
```

Open your browser at `http://localhost:3000` (or the port displayed in terminal).

---

## ✨ Features

- **🧠 Memory Vault & Gallery**:
  - Filter by media type (PDF Documents, Image OCR, WhatsApp Chat logs, Text).
  - Search by keyword or extracted content.
  - Sort by Newest, Oldest, or Name.
  - Interactive full memory modal with image previews, formatted extracted text, raw JSON metadata, and 384-dimensional vector coordinate inspection.
  - Instant one-click copy and deletion tools.

- **💬 Neural Conversational AI (RAG)**:
  - Ask questions in natural language.
  - Dynamic suggestion chips for instant querying.
  - Memory citation cards displaying the exact source documents used to formulate the AI response with confidence indicators.

- **🔍 Dense Semantic & Conceptual Search**:
  - Search by human intent and meaning rather than strict keywords.
  - Live vector similarity score meters (e.g. `96% match`).
  - Jump directly from search results to AI Chat for follow-up questions.

- **📤 Multimodal Ingestion Center**:
  - Drag-and-drop file upload with live extraction progress.
  - Supports `.jpg`, `.png`, `.webp` (Tesseract OCR), `.pdf` (PyMuPDF parser), and `.txt` (WhatsApp chat transcripts).
  - Immediate visual indexing feedback with confetti animation.

- **⚡ Vector Space Laboratory**:
  - Test embeddings on custom text via `POST /embed`.
  - Visual dimension meters for SentenceTransformers (`all-MiniLM-L6-v2`).

---

## 🛠️ Architecture & Tech Stack

- **Frontend**: React 18, TypeScript, Vite, Tailwind CSS, Lucide Icons, Axios, Canvas Confetti.
- **Backend**: FastAPI, Uvicorn, SentenceTransformers, FAISS, PyMuPDF, Tesseract OCR.
