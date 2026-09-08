from ingestion.loader import DocLoader
from ingestion.chunker import Chunker


Loader = DocLoader("C:/Users/Nidhish/Projects/RAG-Multi-Corpus/RAG-Multi-Corpus-main/datasets")
documents = Loader.PDFload()

print(f"Loaded {len(documents)} documents")

Chunker = Chunker(
    chunk_size = 1000,
    chunk_overlap = 200
)
chunks = Chunker.split(documents)

print(f"Created {len(chunks)} chunks")