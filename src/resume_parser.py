from pypdf import PdfReader
from docx import Document
import os


def extract_pdf_text(file_path):
    """Extract text from a PDF resume."""
    text = ""

    reader = PdfReader(file_path)

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text.strip()


def extract_docx_text(file_path):
    """Extract text from a DOCX resume."""
    text = ""

    document = Document(file_path)

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            text += paragraph.text + "\n"

    return text.strip()


def extract_resume_text(file_path):
    """Extract resume text based on file extension."""
    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return extract_pdf_text(file_path)

    elif extension == ".docx":
        return extract_docx_text(file_path)

    else:
        raise ValueError(
            "Unsupported file format. Please upload a PDF or DOCX file."
        )