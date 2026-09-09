from sentence_transformers import SentenceTransformer

class Embedder:

    def __init__(self):
        self.model =  SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

    def embed(self, chunks):
        return self.model.encode(
            chunks, normalize_embeddings = True
            )