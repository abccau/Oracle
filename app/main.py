from ingestion.loader import DocLoader
from ingestion.chunker import Chunker
from ingestion.embeder import Embedder
from qdrant.create_collection import VectorDB
from retrieval.retriver import Retriver
from generation.llm import LLM

### This is a Loader
# Loader = DocLoader("C:/Users/Nidhish/Projects/RAG-Multi-Corpus/RAG-Multi-Corpus-main/datasets")
# documents = Loader.PDFload()
# print(f"Loaded {len(documents)} documents")




# ### This is used to Split
# chunker = Chunker(
#     chunk_size = 1000,
#     chunk_overlap = 200
# )
# chunks = chunker.split(documents)
# print(f"Created {len(chunks)} chunks")

# #### Here Every object is like chunk[0], chunk[1].....
# #### But The embedder expected list of strings like --> ["txt1", "txt2", "txt3...."]
# #### So we will create and pass such list

# texts = []
# for chunk in chunks:
#     texts.append(chunk.page_content)


# ### This is used to Embed
Embed = Embedder()
# embeddings = Embed.embed(texts)
# print(len(embeddings))


# vectordb = VectorDB()
# vectordb.create_collection()
# vectordb.create_points(chunks, embeddings)
# vectordb.print_count


query = "What are the official University Holidays in 2024-2025"
query_embedding = Embed.embed(query)
retrived = Retriver()
points = retrived.search(query_embedding)
# for point in points:
#     print("=" * 50)
#     print(f"Score: {point.score}")
#     print(f"Company: {point.payload['company']}")
#     print(point.payload['text'])
#     print()
context = retrived.build_context(points)

generator = LLM()
answer = generator.generate(context, query)
print(answer.content)