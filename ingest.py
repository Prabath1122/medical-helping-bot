from services.pdf_service import extract_text
from services.embedding_service import create_embeddings
from services.pinecone_service import Index
import uuid

text = extract_text("documents/medicine.pdf")

chunks=[]
chunk_size = 500

for i in range(0,len(text),chunk_size):
    chunks.append(text[i:i+chunk_size])

print(f"Total chunks created: {len(chunks)}")

vectors =[]
for chunk in chunks:
    embedding = create_embeddings(chunk)

    vectors.append({
        "id":str(uuid.uuid4()),
        "values": embedding,
        "metadata":{
            "text": chunk
        }
    })

Index.upsert(vectors=vectors)

print("Data Uploaded successfully")