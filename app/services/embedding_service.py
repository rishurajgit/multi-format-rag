from langchain_google_genai import GoogleGenerativeAIEmbeddings

from config import settings


class EmbeddingService:

    def __init__(self):
        self.embedding_model = GoogleGenerativeAIEmbeddings(
            model=settings.EMBEDDING_MODEL,
            google_api_key=settings.GEMINI_API_KEY,
        )

    def get_embeddings(self):
        """
        Return the embedding model.
        """
        return self.embedding_model