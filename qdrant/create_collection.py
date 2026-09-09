from qdrant_client import QdrantClient, models

class VectorDB:
    def __init__(self):

        self.client = QdrantClient(
            host = "localhost",
            port = 6333
        )