import os
import shutil

from fastapi import APIRouter, File, UploadFile, HTTPException

from config import settings
from app.services.document_service import DocumentService

router = APIRouter()

document_service = DocumentService()


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    file_path = os.path.join(settings.UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    total_chunks = document_service.process_pdf(file_path)

    return {
        "message": "PDF uploaded successfully",
        "chunks": total_chunks,
    }