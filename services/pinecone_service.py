from dotenv import load_dotenv
from pinecone import Pinecone,ServerlessSpec
import os

load_dotenv()


pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY"),
)

if 'medical-data' not in pc.list_indexes().names():
    pc.create_index(
        name="medical-data",
        dimension=768,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

Index = pc.Index("medical-data")