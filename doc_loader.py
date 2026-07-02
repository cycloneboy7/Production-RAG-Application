import os
import tempfile

from pathlib import Path
from langchain_community.document_loaders import (TextLoader)
from dotenv import load_dotenv
load_dotenv()

#text file loaders
def load_text_file():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
        temp_file.write(b"This is a sample text file for testing.")
        temp_file_path = temp_file.name
    try:
        loader = TextLoader(temp_file_path)
        doc = loader.load()
        for i in doc:
            print(i.page_content)
    finally:
        os.unlink(temp_file_path)