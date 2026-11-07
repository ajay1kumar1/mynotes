# My Notes — AI & ML Reference

Personal notes and notebooks covering AI tooling, RAG architectures, and practical guides for running large language models.

---

## Contents

### [`typeOfRags.ipynb`](./typeOfRags.ipynb) — Comprehensive Guide to RAG Architectures

A Jupyter notebook that walks through seven Retrieval-Augmented Generation (RAG) patterns, from the simplest pipeline to graph-based retrieval. Each architecture includes working Python code using LangChain, FAISS, and HuggingFace, along with a comparison table covering complexity, latency, accuracy, and best use cases.

**Architectures covered:**

| # | Architecture | Key Idea | Best For |
|---|---|---|---|
| 1 | **Basic Naive RAG** | Embed → search vector DB → generate | Simple Q&A, fast prototyping |
| 2 | **Hybrid Search RAG** | Vector search + BM25 keyword search, merged | Semantic + exact keyword match |
| 3 | **RAG with Reranking** | Cross-encoder re-scores top-k results before generation | High-precision retrieval |
| 4 | **Query Expansion RAG** | LLM rewrites/splits query before retrieval (HyDE) | Complex or ambiguous questions |
| 5 | **Agentic RAG** | LLM agent plans retrieval strategy dynamically | Multi-step reasoning, tool use |
| 6 | **GraphRAG** | Knowledge graph + vector search over entities | Relationship queries, multi-hop |
| 7 | **Multi-Stage / Tiered RAG** | Routes query to fast cache, vector, or graph by complexity | Mixed workload optimization |

**Dependencies:**
```bash
pip install langchain langchain-community langchain-chroma sentence-transformers \
            faiss-cpu pandas matplotlib chromadb python-dotenv rank-bm25 networkx \
            langchain-huggingface langgraph langchain-cohere
```

---

### [`ClaudeFree.txt`](./ClaudeFree.txt) — Run Claude Code for Free (13-Step Guide)

A step-by-step guide to running Claude Code using entirely free AI models — no paid Claude subscription required. Covers Windows (with a Mac-compatible bonus section).

**What it sets up:**

- **OpenRouter** — single API key giving access to dozens of free models
- **OmniRoute** — local proxy that round-robins across free providers; when one hits its daily limit, it auto-switches to the next
- **NVIDIA NIM** — free-tier models (e.g., `gpt-oss-120b`) via NVIDIA Build
- **Ollama** — fully offline, local model inference for machines with 6 GB+ VRAM
- **Kilo Code** — VS Code extension as an alternative free AI coding assistant

**Guide outline:**

| Step | Topic |
|------|-------|
| 1 | Prerequisites (Windows PC, free accounts — no card needed) |
| 2 | Get a free OpenRouter API key |
| 3 | Start Claude Code pointed at free models via OpenRouter |
| 4 | Install OmniRoute with Antigravity (Google's free coding app) |
| 5 | Connect NVIDIA NIM and OpenRouter as providers in OmniRoute |
| 6 | Build a combo that auto-switches models on rate-limit |
| 7 | Create a one-click Desktop shortcut for Free Claude Code |
| 8 | Build your first app with a sample prompt |
| 9 | *(Optional)* Run a local model offline with Ollama |
| 10 | *(Optional)* Install Kilo Code in VS Code |
| 11 | *(Optional)* Connect free NVIDIA models to Kilo Code |
| 12 | *(Optional)* Build a full 2D space shooter game (NEON VOID) in one prompt |
| 13 | *(Optional)* Keep building when a model hits its rate limit |

**Tools referenced:** Claude Code · OpenRouter · Antigravity · OmniRoute · NVIDIA Build · Ollama · VS Code · Kilo Code · Google AI Studio

---

## Quick Start

```bash
# Clone
git clone https://github.com/ajay1kumar1/mynotes.git
cd mynotes

# Open the notebook
jupyter notebook typeOfRags.ipynb
```

---

## Author

Ajay SR — [github.com/ajay1kumar1](https://github.com/ajay1kumar1)
