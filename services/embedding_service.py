from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-mpnet-base-v2')

def create_embeddings(text):
    return model.encode(text).tolist()