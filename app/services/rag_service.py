from langchain_google_genai import ChatGoogleGenerativeAI

from config import settings
from app.core.prompt import RAG_PROMPT
from app.services.retriever_service import RetrieverService

class RAGService:
    def __init__(self):
        self.retriever = RetrieverService() #gives access to ChromaDB
        
        self.llm = ChatGoogleGenerativeAI(
            model = settings.LLM_MODEL,
            google_api_key = settings.GEMINI_API_KEY,
            temperature = 0
        )
        
    def generate_response(self, question: str):
        
        documents = self.retriever.retrieve_documents(question)
        context = "\n\n".join(
            document.page_content
            for document in documents
        )
        
        prompt = RAG_PROMPT.format(
            context = context,
            question = question
        )
        
        response = self.llm.invoke(prompt)
        
        return{
            "answer": response.content,
            "sources": [
                {
                
                "document_name": document.metadata.get("document_name"),
                "page": document.metadata.get("page"),
                "chunk_id": document.metadata.get("chunk_id"),
        }
        for document in documents
            ]
                
        }