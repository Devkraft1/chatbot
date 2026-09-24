import chromadb

client = chromadb.PersistentClient(path="./chroma_data")
collection = client.get_or_create_collection("documents")

def search(query: str, n_results: int = 5):
    results = collection.query(
        query_texts=[query],
        n_results=n_results,
        include=["documents", "metadatas"]
    )
    formatted_results = []
    for i in range(len(results["documents"][0])):
        formatted_results.append({
            "path": results["metadatas"][0][i]["path"],
            "description": results["documents"][0][i]
        })
    return formatted_results