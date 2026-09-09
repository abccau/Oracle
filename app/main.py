from ingestion.loader import DocLoader
from ingestion.chunker import Chunker
from ingestion.embeder import Embedder



### This is a Loader
Loader = DocLoader("C:/Users/Nidhish/Projects/RAG-Multi-Corpus/RAG-Multi-Corpus-main/datasets")
documents = Loader.PDFload()
print(f"Loaded {len(documents)} documents")




### This is used to Split
chunker = Chunker(
    chunk_size = 1000,
    chunk_overlap = 200
)
chunks = chunker.split(documents)
print(f"Created {len(chunks)} chunks")

#### Here Every object is like chunk[0], chunk[1].....
#### But The embedder expected list of strings like --> ["txt1", "txt2", "txt3...."]
#### So we will create and pass such list

texts = []
for chunk in chunks:
    texts.append(chunk.page_content)


### This is used to Embed
Embed = Embedder()
embeddings = Embed.embed(texts)
print(len(embeddings))