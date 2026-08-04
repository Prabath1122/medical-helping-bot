from dotenv import load_dotenv
from flask import Flask, jsonify, request
from services.pinecone_service import Index
import os
from services.rag_service import query_rag

from services.embedding_service import create_embeddings
from twilio.twiml.messaging_response import MessagingResponse

load_dotenv()
key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/')
def home():
     return jsonify({
        "success": True,
        "message": "API is running successfully"
    })

@app.route('/hello')
def hello():
    return jsonify({
        "success": True,
        "message": "Hello, World!"
    })


@app.route('/ask',methods=['POST'])
def ask():
    data = request.get_json()
    print(data)
    question = data.get("question")

    answer = query_rag(question)

    # embeddings = create_embeddings(question)

    # result= Index.query(
    #     vector=embeddings,
    #     top_k=5,
    #     include_metadata=True
    # )

    return jsonify({
        "success": True,
        "question": question,
        "answer": answer
    })


@app.route

@app.route('/whatapp', methods=['POST'])
def whatapp():
    question = request.form.get('Body')
    print("Received question:", question)
    answer= query_rag(question)
    response= MessagingResponse()
    response.message(answer)
    return str(response)
    # return "ok connected", 200

if __name__=="__main__":
    app.run(debug=True)


