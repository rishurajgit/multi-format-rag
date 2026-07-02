from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import settings


class TextSplitter:

    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
        )

    def split_documents(self, documents):
        """
        Split the loaded documents into smaller chunks.
        """
        return self.text_splitter.split_documents(documents)