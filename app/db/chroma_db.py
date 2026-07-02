from langchain_chroma import Chroma

from config import settings
from app.services.embedding_service import EmbeddingService


class ChromaDB:

    def __init__(self):
        embedding_service = EmbeddingService()

        self.vector_store = Chroma(
            collection_name="documents",
            embedding_function=embedding_service.get_embeddings(),
            persist_directory=settings.CHROMA_DB_PATH,
        )

    def get_vector_store(self):
        """
        Return the Chroma vector store.
        """
        return self.vector_store