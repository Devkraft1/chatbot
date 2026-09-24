import chromadb
import uuid
client = chromadb.PersistentClient(path="./chroma_data")
collection = client.get_or_create_collection("documents")
def add_entry(description, path="", url=""):
    entryId = str(uuid.uuid4())
    collection.upsert(
        ids=[entryId],
        documents=[description],
        metadatas=[{
            "path": path,
            "url": url
        }]
    )