from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv
from llm import ask_llm

load_dotenv()

pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY")
)

index = pc.Index("medical-data")

model = SentenceTransformer(
    "sentence-transformers/all-mpnet-base-v2"
)

question = "What are the medicines for cold cough?"

embedding = model.encode(question).tolist()

results = index.query(
    vector=embedding,
    top_k=3,
    include_metadata=True
)

context =""

for match in results.matches:
    context += match.metadata["text"]
    context += "\n\n"

prompt = f"""
Answer the question using only the provided context.

Context:
{context}

Question:
{question}
"""

answer = ask_llm(prompt)
print(answer)