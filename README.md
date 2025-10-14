# 🧠 RAG Assistant – Your Intelligent Knowledge Companion

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)  
![Streamlit](https://img.shields.io/badge/Streamlit-0.120-orange?logo=streamlit&logoColor=white)  
![LangChain](https://img.shields.io/badge/LangChain-1.0-lightgrey)  
![Chroma](https://img.shields.io/badge/Chroma-VectorDB-blue)  
![Pinecone](https://img.shields.io/badge/Pinecone-CloudDB-red)  
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🚀 About

**RAG Assistant** is a **Retrieval-Augmented Generation (RAG) assistant** that combines **LangChain**, **Tavily**, **Chroma**, **Pinecone**, and **Streamlit** to provide accurate, context-aware answers.  

It can:  

- Scrape LangChain documentation via **Tavily**.  
- Embed documents using **Chroma** (local) or **Pinecone** (cloud).  
- Perform semantic **similarity search** for fast retrieval.  
- Generate human-like answers using **LLM**.  
- Serve queries through a beautiful **Streamlit interface**.  

---

## 🔥 Features

- **LangChain Powered:** Advanced RAG workflows for accurate answers.  
- **Tavily Web Scraping:** Automatically searches and scrapes LangChain docs.  
- **Vector Databases:** Local search via Chroma, cloud scalability via Pinecone.  
- **Streamlit Frontend:** Interactive UI for seamless question answering.  
- **Semantic Similarity Search:** Finds relevant content across documents and web.  
- **Custom Knowledge Base:** Upload your own files to expand the assistant.  

---

## 🛠 Tech Stack

| Component              | Technology/Tool                        |
|------------------------|----------------------------------------|
| **LLM Framework**      | LangChain                              |
| **Web Scraping**       | Tavily                                 |
| **Vector DB**          | Chroma (local), Pinecone (cloud)      |
| **Embeddings**         | Google Gemini / OpenAI embeddings      |
| **Frontend**           | Streamlit                              |
| **Search**             | Semantic similarity search             |
| **Deployment**         | Local / Cloud-ready                    |

---

## ⚡ Installation

1. **Clone the repository**

```bash
git clone https://github.com/arnavsinghtomar/RAG-assistant.git
cd RAG-assistant
```
2. **Install dependencies**
```bash
pip install -r requirements.txt
```
3. **Set environment variables in a .env file**
```bash
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

🖥 Usage

Run the Streamlit app:
```bash
streamlit run app.py
```
Steps:

🔹 Scrape LangChain docs using Tavily.

🔹 Embed documents into Chroma (local) or Pinecone (cloud).

🔹 Ask questions via the Streamlit interface and get context-aware answers.

🔹 Upload additional documents to expand the knowledge base.

Example query in the app:
```bash
"How do I use LangChain's RetrievalQA chain with a vector store?"
```

---

🔍 How It Works

1. Web Scraping: Tavily searches and scrapes the latest LangChain documentation.

2. Embedding: Chroma or Pinecone converts documents into vector embeddings.

3. Semantic Search: Finds the most relevant content chunks for queries.

4. Generative Response: LangChain LLM produces accurate answers using retrieved context.

 ---

📁 File Structure
```bash
RAG-assistant/
├─ app.py                # Streamlit frontend
├─ tavily_scraper.py     # Scrapes LangChain docs
├─ ingestion.py          # Local document ingestion
├─ utils.py              # Helper functions
├─ requirements.txt      # Dependencies
├─ README.md             # Project documentation
└─ .env                  # API keys (ignored)
```
✨ Future Enhancements

🌐 Real-time updates from LangChain docs.

📚 Multi-document summarization for richer answers.

🧩 Advanced query parsing with LangChain chains.

☁ Full cloud deployment with authentication and multi-user support.

---

🎬 Demo

Replace assets/demo.gif with your actual demo GIF or screenshot.

---

🏆 Why It’s Cool

🔥 Always up-to-date with LangChain docs.

⚡ Fast, intelligent responses using vector search + LLM.

🗂 Fully customizable knowledge base.

☁ Scalable via Pinecone for large datasets.

---

📜 License

This project is licensed under the MIT License – see the LICENSE file for details.




