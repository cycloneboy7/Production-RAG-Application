# Production RAG Application

A production-ready Retrieval-Augmented Generation (RAG) application that allows users to upload documents and ask questions using natural language. The system combines hybrid retrieval (BM25 + vector search), cross-encoder reranking, citation-aware responses, and an automated evaluation pipeline to provide accurate and reliable answers.

> **Status:** 🚧 Work in Progress

---

## Features

* 📄 Upload PDF, DOCX, TXT, and Markdown documents
* 🔍 Hybrid retrieval using BM25 + Vector Search
* 🎯 Cross-encoder reranking for improved search relevance
* 📚 Citation-aware answers with document and page references
* 💬 Chat interface with conversation history
* ⚡ Streaming AI responses
* 🔐 User authentication
* 📊 Monitoring and evaluation metrics
* 🧪 CI pipeline with automated regression testing
* 🐳 Docker support for easy deployment

---

## Tech Stack

### Backend

* Python
* FastAPI
* LangChain
* PostgreSQL
* Qdrant Vector Database

### AI

* OpenAI / Gemini / Ollama (provider interchangeable)
* BAAI Embedding Models
* BM25
* Cross Encoder Reranker

### Frontend

* Next.js
* React
* TypeScript
* Tailwind CSS

### DevOps

* Docker
* GitHub Actions
* Pytest

---

## Architecture

```
User
   │
   ▼
Frontend (Next.js)
   │
   ▼
FastAPI Backend
   │
   ├── Document Upload
   ├── Text Extraction
   ├── Chunking
   ├── Embedding Generation
   ├── Hybrid Retrieval
   ├── Cross Encoder Reranking
   ├── LLM Response Generation
   └── Citation Enforcement
   │
   ▼
Response with Sources
```

---

## Project Structure

```
production-rag/
│
├── backend/
│   ├── api/
│   ├── retrieval/
│   ├── embeddings/
│   ├── reranker/
│   ├── evaluation/
│   ├── services/
│   ├── tests/
│   └── main.py
│
├── frontend/
│   ├── app/
│   ├── components/
│   └── hooks/
│
├── datasets/
├── benchmarks/
├── docs/
├── docker/
├── .github/
│   └── workflows/
├── docker-compose.yml
└── README.md
```

---

## How It Works

1. Upload one or more documents.
2. Documents are parsed and split into chunks.
3. Embeddings are generated and stored in the vector database.
4. A BM25 index is created for keyword search.
5. User submits a question.
6. Hybrid retrieval fetches relevant chunks.
7. Cross-encoder reranking selects the best context.
8. The LLM generates an answer using only the retrieved information.
9. Citations are attached to every response.

---

## Example

**Question**

```
How many paid sick leaves does an employee receive?
```

**Answer**

```
Employees are entitled to 12 paid sick leaves per calendar year.

Sources:
• Employee Handbook – Page 24
• HR Policy – Page 11
```

---

## Evaluation

The project includes an automated evaluation pipeline to measure retrieval and answer quality.

Metrics include:

* Recall@K
* Precision
* Faithfulness
* Context Precision
* Answer Relevancy
* Response Latency

Every pull request runs these evaluations automatically to detect performance regressions.

---

## Running Locally

Clone the repository:

```bash
git clone https://github.com/yourusername/production-rag.git
cd production-rag
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENAI_API_KEY=
GEMINI_API_KEY=
QDRANT_URL=
QDRANT_API_KEY=
```

Run the backend:

```bash
uvicorn main:app --reload
```

Or start everything using Docker:

```bash
docker compose up
```

---

## Roadmap

* [ ] Document upload
* [ ] PDF parsing
* [ ] Hybrid retrieval
* [ ] Cross-encoder reranking
* [ ] Citation enforcement
* [ ] Authentication
* [ ] Chat history
* [ ] Streaming responses
* [ ] Evaluation pipeline
* [ ] Monitoring dashboard
* [ ] Docker deployment
* [ ] GitHub Actions CI/CD

---

## Future Improvements

* OCR support for scanned PDFs
* Multi-language retrieval
* Role-based access control
* Semantic caching
* Document versioning
* Voice input
* Multi-modal document support
* Feedback collection for continuous improvement


This project is licensed under the MIT License.
