from dotenv import load_dotenv
from pypdf import PdfReader

path = "/Users/vaibhavisavani/Desktop/Gen-AI/RAG-Comparision/data/The-Ultimate-Skin-Care-Routine-Guide-_-SELF.pdf"


def read_data(path=path):
    reader = PdfReader(path)
    data = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            data += text

    return data