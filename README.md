# 🏥 Medical AI RAG Chatbot

A Python-based **Medical Question Answering System** built using **Retrieval-Augmented Generation (RAG)**.

The system extracts medical information from PDF documents, converts the content into vector embeddings, stores the embeddings in **Pinecone**, and uses an LLM through **OpenRouter** to generate answers based on the retrieved medical context.

The application also provides a **Flask REST API** and supports **WhatsApp integration through Twilio**.

---

## 📌 Overview

This project demonstrates how to build a RAG-based AI application that answers questions using information from a custom medical knowledge base.

Instead of sending a user's question directly to an LLM, the system first searches the medical knowledge stored in Pinecone and retrieves the most relevant information.

### Basic Flow

```text
Medical PDF
     │
     ▼
Extract Text
     │
     ▼
Split into Chunks
     │
     ▼
Generate Embeddings
     │
     ▼
Pinecone Vector Database
     │
     │
     ▼
User Question
     │
     ▼
Generate Question Embedding
     │
     ▼
Semantic Search in Pinecone
     │
     ▼
Retrieve Relevant Medical Information
     │
     ▼
Build Prompt
     │
     ▼
OpenRouter / GPT-4.1-mini
     │
     ▼
Generate Answer
     │
     ▼
User
```

---

## ✨ Features

* 📄 Extract text from medical PDF documents
* ✂️ Split documents into smaller chunks
* 🧠 Generate text embeddings using Sentence Transformers
* 🔎 Perform semantic similarity search
* 🗄️ Store and retrieve vectors using Pinecone
* 🤖 Generate answers using an LLM through OpenRouter
* 🌐 Flask REST API
* 💬 WhatsApp integration using Twilio
* 🔐 Environment-based API key configuration
* 🧩 Modular Python project structure

---

## 🛠️ Technologies Used

| Technology            | Purpose                         |
| --------------------- | ------------------------------- |
| Python                | Main programming language       |
| Flask                 | REST API / backend server       |
| PyPDF                 | Extract text from PDF files     |
| Sentence Transformers | Generate text embeddings        |
| `all-mpnet-base-v2`   | Embedding model                 |
| Pinecone              | Vector database                 |
| OpenRouter            | LLM API provider                |
| GPT-4.1-mini          | AI response generation          |
| Twilio                | WhatsApp integration            |
| python-dotenv         | Environment variable management |

---

# 🧠 What is RAG?

RAG stands for:

> **Retrieval-Augmented Generation**

Instead of asking an AI model to answer a question using only its existing knowledge, RAG first retrieves relevant information from an external knowledge source.

### Without RAG

```text
User Question
     │
     ▼
    LLM
     │
     ▼
   Answer
```

### With RAG

```text
User Question
     │
     ▼
Create Embedding
     │
     ▼
Search Vector Database
     │
     ▼
Retrieve Relevant Context
     │
     ▼
Question + Context
     │
     ▼
    LLM
     │
     ▼
   Answer
```

This project follows the second approach.

---

# 🔄 Application Flow

## 1. Document Ingestion

The medical PDF is processed using `ingest.py`.

```text
medicine.pdf
     ↓
Extract text
     ↓
Split text into chunks
     ↓
Generate embeddings
     ↓
Store vectors in Pinecone
```

The ingestion process only needs to be performed when the knowledge source is initially added or updated.

---

## 2. User Question

A user can submit a question through the REST API or WhatsApp.

Example:

```text
What medicines are commonly used for a cold?
```

---

## 3. Question Embedding

The question is converted into a vector using:

```text
sentence-transformers/all-mpnet-base-v2
```

Conceptually:

```text
"What medicines are commonly used for a cold?"
                    ↓
             Embedding Model
                    ↓
          [0.12, -0.43, 0.78, ...]
```

---

## 4. Semantic Search

The question embedding is sent to Pinecone.

The system searches for the most semantically relevant chunks of medical information.

The current implementation retrieves:

```text
Top 3 relevant chunks
```

---

## 5. Context Construction

The retrieved text is combined into a context.

Conceptually:

```text
Context:

Medical information chunk 1...

Medical information chunk 2...

Medical information chunk 3...
```

---

## 6. LLM Generation

The system combines the retrieved context with the user's question.

```text
Context
   +
Question
   ↓
Prompt
   ↓
OpenRouter
   ↓
GPT-4.1-mini
   ↓
Answer
```

---

# 📂 Project Structure

```text
project/
│
├── app.py
├── ingest.py
├── query.py
├── llm.py
├── requirements.txt
├── .env
├── .gitignore
│
├── documents/
│   └── medicine.pdf
│
└── services/
    ├── embedding_service.py
    ├── pdf_service.py
    ├── pinecone_service.py
    └── rag_service.py
```

---

# 📄 File Responsibilities

### `app.py`

Main Flask application.

Provides API endpoints for:

* Health checking
* Question answering
* WhatsApp webhook integration

Main RAG endpoint:

```text
POST /ask
```

WhatsApp endpoint:

```text
POST /whatapp
```

---

### `ingest.py`

Responsible for preparing the medical knowledge base.

It:

1. Reads the medical PDF
2. Extracts text
3. Splits the text into chunks
4. Generates embeddings
5. Uploads the vectors to Pinecone

---

### `query.py`

Standalone script for testing the RAG pipeline without using the Flask API.

It can be useful when testing:

```text
Question
   ↓
Embedding
   ↓
Pinecone
   ↓
Retrieved Context
   ↓
LLM
   ↓
Answer
```

---

### `llm.py`

Handles communication with the LLM through OpenRouter.

The project uses:

```text
OpenRouter
    ↓
openai/gpt-4.1-mini
```

---

### `services/pdf_service.py`

Responsible for extracting text from PDF files using PyPDF.

---

### `services/embedding_service.py`

Responsible for generating embeddings using:

```text
sentence-transformers/all-mpnet-base-v2
```

The model produces a **768-dimensional vector**.

---

### `services/pinecone_service.py`

Handles the connection to Pinecone and the vector index.

The project uses:

```text
Index: medical-data
Metric: cosine
Dimension: 768
```

---

### `services/rag_service.py`

This is the central RAG logic.

It:

1. Converts the question into an embedding
2. Searches Pinecone
3. Retrieves relevant documents
4. Builds the context
5. Creates the LLM prompt
6. Sends the prompt to the LLM
7. Returns the generated answer

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Move into the project directory:

```bash
cd YOUR_REPOSITORY
```

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory.

Example:

```env
PINECONE_API_KEY=your_pinecone_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
```

### Important

Never commit your `.env` file to GitHub.

Add this to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

---

# 📚 Prepare the Knowledge Base

Place your medical PDF inside:

```text
documents/
```

For example:

```text
documents/
└── medicine.pdf
```

Then run:

```bash
python ingest.py
```

This will:

```text
PDF
 ↓
Extract text
 ↓
Create chunks
 ↓
Generate embeddings
 ↓
Upload vectors
 ↓
Pinecone
```

Once ingestion is complete, your medical information is available for semantic search.

---

# 🚀 Run the Application

Start the Flask application:

```bash
python app.py
```

The API should then be available locally through the Flask server.

---

# 🧪 Testing the API

You can test the `/ask` endpoint using Postman, Insomnia, curl, or another HTTP client.

### Request

```http
POST /ask
Content-Type: application/json
```

Body:

```json
{
  "question": "What medicines are commonly used for a cold?"
}
```

### Example Response

```json
{
  "success": true,
  "question": "What medicines are commonly used for a cold?",
  "answer": "..."
}
```

---

# 💬 WhatsApp Integration

The application also supports WhatsApp through **Twilio**.

The basic architecture is:

```text
WhatsApp User
      ↓
    Twilio
      ↓
/whatapp endpoint
      ↓
query_rag()
      ↓
Pinecone
      ↓
OpenRouter
      ↓
GPT-4.1-mini
      ↓
Twilio
      ↓
WhatsApp User
```

Configure your Twilio WhatsApp webhook to point to the deployed Flask endpoint:

```text
https://your-domain.com/whatapp
```

---

# 🔍 Example RAG Flow

Suppose the user asks:

```text
What medicines can help with a headache?
```

The system performs:

```text
1. Receive question
        ↓
2. Generate embedding
        ↓
3. Search Pinecone
        ↓
4. Retrieve top 3 relevant chunks
        ↓
5. Build context
        ↓
6. Add question to prompt
        ↓
7. Send prompt to OpenRouter
        ↓
8. GPT-4.1-mini generates response
        ↓
9. Return answer
```

---

# 🧩 RAG Components

The core RAG pipeline can be summarized as:

```text
Document
   ↓
Chunking
   ↓
Embedding
   ↓
Vector Database
   ↓
Retrieval
   ↓
Context
   ↓
LLM
   ↓
Generation
```

---

# 🏗️ Architecture

```text
                         ┌─────────────────┐
                         │  Medical PDF    │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │   ingest.py     │
                         └────────┬────────┘
                                  │
                         Text Extraction
                                  │
                                  ▼
                         ┌─────────────────┐
                         │ Text Chunking   │
                         └────────┬────────┘
                                  │
                                  ▼
                    ┌──────────────────────────┐
                    │ Sentence Transformers   │
                    │   all-mpnet-base-v2      │
                    └────────────┬─────────────┘
                                 │
                            Embeddings
                                 │
                                 ▼
                         ┌──────────────┐
                         │   Pinecone   │
                         │ Vector Store │
                         └───────┬──────┘
                                 ▲
                                 │
                         Semantic Search
                                 │
User ────────► Flask API ───────┘
                  │
                  ▼
             rag_service.py
                  │
                  ▼
            Retrieved Context
                  │
                  ▼
               llm.py
                  │
                  ▼
             OpenRouter
                  │
                  ▼
             GPT-4.1-mini
                  │
                  ▼
               Response
```

---

# 🔐 Security Considerations

API keys should always be stored in environment variables.

Do not commit:

```text
.env
API keys
Twilio credentials
Pinecone credentials
OpenRouter credentials
```

Use:

```text
.gitignore
```

to prevent accidental commits.

---

# ⚠️ Medical Disclaimer

This project is intended for **educational and software-development purposes**.

The generated responses should not be considered a substitute for professional medical advice, diagnosis, or treatment.

A production medical application should include appropriate medical validation, safety controls, monitoring, privacy protection, and professional review before being used with real patients.

---

# 🚀 Possible Future Improvements

Potential improvements include:

* Better document chunking with overlap
* Sentence/paragraph-aware chunking
* Metadata filtering
* Source citations in generated answers
* Conversation memory
* Authentication and authorization
* Request validation
* Rate limiting
* Better error handling
* Logging and monitoring
* Streaming LLM responses
* Multiple medical document collections
* Improved prompt engineering
* Evaluation of RAG retrieval accuracy
* Re-ranking retrieved documents
* Production deployment using Docker
* HTTPS and secure webhook validation
* More robust medical safety guardrails

---

# 🧠 Important Note

This project implements the RAG pipeline **directly using Python libraries and APIs**.

It does **not currently use LangChain**.

The main components are integrated directly:

```text
Sentence Transformers
        +
Pinecone
        +
OpenRouter
        +
Flask
        +
Twilio
```

This makes the project a useful example of implementing a RAG pipeline without relying on a framework such as LangChain.

---

# 👨‍💻 Author

**Akila Prabath**

Software Engineer | React.js | Node.js | Python | AI/ML | RAG

---

## ⭐ If you find this project useful

Feel free to ⭐ star the repository and use the architecture as a reference for building RAG-based AI applications.
