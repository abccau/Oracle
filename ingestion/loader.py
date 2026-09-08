from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyPDFDirectoryLoader
from pathlib import Path
import os



class DocLoader:

    def __init__(self, dataset_path):
        self.dataset_path = Path(dataset_path)
        

    def PDFload(self):

        all_docs = []
        for item in self.dataset_path.iterdir():
            if not item.is_dir():
                continue

            pdf_dir = item / "pdf"

            if not pdf_dir.is_dir():
                continue
            else :
                Loader = PyPDFDirectoryLoader(str(pdf_dir))
                docs = Loader.load()

                for doc in docs:
                    doc.metadata["Company"] = item.name

                all_docs.extend(docs)

        return all_docs



