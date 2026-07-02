from app.loaders.document_loader import DocumentLoader
from app.processing.splitter import TextSplitter
from app.db.chroma_db import ChromaDB
import os


class DocumentService:

    def __init__(self):
        self.loader = DocumentLoader()
        self.splitter = TextSplitter()
        self.vector_store = ChromaDB().get_vector_store()

    def process_pdf(self, file_path: str):
        """
        Load the PDF, split it into chunks,
        and store the chunks in ChromaDB.
        """

        documents = self.loader.load_pdf(file_path)
        
        total_pages = len(documents)

        chunks = self.splitter.split_documents(documents)
        
        document_name = os.path.basename(file_path)
        for index, chunk in enumerate(chunks):
            chunk.metadata["document_name"] = document_name
            chunk.metadata["chunk_id"] = index + 1 #instead of 0,1,2 we get 1,2,3

        self.vector_store.add_documents(chunks)

        return {
            "document_name": document_name,
            "total_pages": total_pages,
            "total_chunks": len(chunks)
        }