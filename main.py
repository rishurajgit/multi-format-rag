
#JUST CHECKING

# from config import settings

# print(f"Model: {settings.LLM_MODEL}")
# print(f"Embedding Model: {settings.EMBEDDING_MODEL}")
# print(f"Chunk Size: {settings.CHUNK_SIZE}")
# print(f"Upload Directory: {settings.UPLOAD_DIR}")

from fastapi import FastAPI

from app.routes import router

app = FastAPI()

app.include_router(router)