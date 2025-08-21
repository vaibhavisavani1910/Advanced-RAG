# RAG Models Playground

Welcome to my **RAG (Retrieval-Augmented Generation) Models Playground**! ✨  

This repository is a hands-on exploration of different RAG experiments using **LangChain**, **MongoDB Atlas**, and **OpenAI embeddings & LLMs**. The goal is to see how retrieval-based techniques can enhance LLM answers, from simple vector search to hybrid graph-based approaches.

---

## 📁 Notebook Overview

| Notebook | Description |
|----------|-------------|
| **1-Simple-RAG.ipynb** | Classic retrieval-augmented generation: split text into chunks, embed with OpenAI, store in MongoDB, retrieve top-K chunks for query answering. |
| **2-Re-ranking.ipynb** | Adds a re-ranking step: retrieves candidates first, then ranks them with a secondary model for better relevance. |
| **3-Semantic-Chunking.ipynb** | Uses **semantic chunking** to split text based on meaning instead of fixed size, improving retrieval quality. |
| **4-HyDE-RAG.ipynb** | Implements **Hypothetical Document Embeddings (HyDE)**: generates a pseudo-answer to a query, embeds it, and retrieves relevant chunks. |
| **5-Multi-Modal-Captioning.ipynb** | Combines text and image captions for multi-modal RAG retrieval. |
| **6-GraphRAG.ipynb** | Builds a **knowledge graph** from text chunks and retrieves using vector similarity plus graph traversal. Ideal for complex queries requiring entity relationships. |

Made with ❤️ by Vaibhavi Savani.
