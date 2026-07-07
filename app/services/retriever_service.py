from app.db.chroma_db import ChromaDB

class RetrieverService:
    def __init__(self):  #automatically connect to database
        self.vector_store = ChromaDB().get_vector_store()
        
    def retrieve_documents(self, query: str, k: int = 2):
        """
        Retrieve the most relevant document chunks.
        """
        
        documents = self.vector_store.similarity_search(
            query = query,
            k = k
        )
        
        return documents 