from fastapi import FastAPI, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from summarizer import summarize_text
from pathlib import Path

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

chat_history = []
document_context = ""


@app.get("/", response_class=HTMLResponse)
async def home():
    return Path("ui.html").read_text()


@app.post("/paste", response_class=HTMLResponse)
async def paste_handler(text: str = Form(...)):
    global document_context
    document_context = text
    summary = summarize_text(document_context)
    chat_history.append({"user": "[Pasted Document]", "ai": summary})
    return f"<div><b>Pasted/Written Text:</b><br/>{text}<br/><b>AI Summary:</b> {summary}</div>"


@app.post("/upload", response_class=HTMLResponse)
async def upload_file(file: UploadFile = File(...)):
    global document_context
    contents = await file.read()
    document_context = contents.decode("utf-8")
    summary = summarize_text(document_context)
    chat_history.append({"user": f"[Uploaded File: {file.filename}]", "ai": summary})
    return (
        f"<div><b>Uploaded:</b> {file.filename}<br/><b>AI Summary:</b> {summary}</div>"
    )


@app.post("/query", response_class=HTMLResponse)
async def query_handler(query: str = Form(...)):
    if not document_context.strip():
        return (
            "<div style='color:red;'>⚠️ Please upload or paste a document first.</div>"
        )

    # Summarize document (ignoring query for now)
    response = summarize_text(document_context)
    chat_history.append({"user": query, "ai": response})
    return f"<div><b>You asked:</b> {query}<br/><b>AI Summary Based on Document:</b> {response}</div>"
