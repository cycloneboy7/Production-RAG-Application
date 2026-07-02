import os
import tempfile

from pathlib import Path
from langchain_community.document_loaders import (TextLoader)
from dotenv import load_dotenv
load_dotenv()

#text file loaders
def load_text_file(): # def PyPDFLoader(file_path: str):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
        temp_file.write(b"This is a sample text file for testing.")
        temp_file_path = temp_file.name
    try:
        #loader = PyPDFLoader(temp_file_path)
        loader = TextLoader(temp_file_path)
        doc = loader.load()
        for i in doc: #for i,doc in enumerate(doc):
            print(i)
            print(i.page_content)
    finally:
        os.unlink(temp_file_path)
        
        
if __name__ == "__main__":
    load_text_file()
    #PyPDFLoader("sample.pdf")