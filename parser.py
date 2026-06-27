from pypdf import PdfReader

def extract_text(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"
    return text

def extract_job_description(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()