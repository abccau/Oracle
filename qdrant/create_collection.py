from qdrant_client import QdrantClient, models
from qdrant_client.models import VectorParams, Distance, PointStruct


class VectorDB:
    def __init__(self):

        self.client = QdrantClient(
            host = "localhost",
            port = 6333
        )

    def create_collection(self):
        self.client.create_collection(
            collection_name = "qdrant_collection",
            vectors_config = VectorParams(
                size = 384,
                distance = Distance.COSINE
            )
        )

    def create_points(self, chunks, embeddings):
        points = []
        for idx, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
            payload = {
                "text": chunk.page_content,
                "company": chunk.metadata["Company"],
                "source": chunk.metadata.get("Source"),
            }

            points.append(PointStruct(
                    id = idx,
                    vector = embedding.tolist(), ###Converted Numpy Array to Python List
                    payload = payload
                )
            )

        operation_info = self.client.upsert(  ####Created an Object for debugging
            collection_name = "qdrant_collection",
            points = points
        )
        

        return operation_info

    def print_count(self):
        return self.client.count(
            collection_name = "qdrant_collection"
        )
        
    
    