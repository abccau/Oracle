from qdrant_client import QdrantClient, models

class Retriver:
    def __init__(self):
        self.client = QdrantClient(
            host = "localhost",
            port = 6333,
        )

    def search(self, query_embeddings):
        results = self.client.query_points(
            query = query_embeddings,
            collection_name = "qdrant_collection",
        )

        return results.points

    def build_context(self, points):
        context = ""

        for point in points:
            context += point.payload["text"]
            context = "\n\n"

        return context
