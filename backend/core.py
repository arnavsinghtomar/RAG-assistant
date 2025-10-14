
from dotenv import load_dotenv
from typing import Any, Dict, List

from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.retrieval import create_retrieval_chain
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from consts import INDEX_NAME


load_dotenv()


embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
chroma = Chroma(persist_directory="chroma_db", embedding_function=embeddings)




def format_docs(docs):
    """Combine all document text into a single string."""
    return "\n\n".join(doc.page_content for doc in docs)




def run_llm(query: str, chat_history: List[Dict[str, Any]] = []):
    """Run retrieval-augmented generation using LangChain's built-in chains."""
    docsearch = Chroma(persist_directory="chroma_db", embedding_function=embeddings)
    chat = ChatOpenAI(verbose=True, temperature=0)

   
    rephrase_prompt = hub.pull("langchain-ai/chat-langchain-rephrase")
    retrieval_qa_prompt = hub.pull("langchain-ai/retrieval-qa-chat")

   
    stuff_chain = create_stuff_documents_chain(chat, retrieval_qa_prompt)
    history_retriever = create_history_aware_retriever(
        llm=chat, retriever=docsearch.as_retriever(), prompt=rephrase_prompt
    )
    qa_chain = create_retrieval_chain(
        retriever=history_retriever, combine_docs_chain=stuff_chain
    )

    result = qa_chain.invoke({"input": query, "chat_history": chat_history})
    return result

def run_llm2(query: str, chat_history: List[Dict[str, Any]] = []):
    """Run RAG pipeline using custom Runnable chains."""
    docsearch = Chroma(persist_directory="chroma_db", embedding_function=embeddings)
    chat = ChatOpenAI(model="gpt-4o-mini", verbose=True, temperature=0)

   
    rephrase_prompt = hub.pull("langchain-ai/chat-langchain-rephrase")
    retrieval_qa_prompt = hub.pull("langchain-ai/retrieval-qa-chat")

    retriever = docsearch.as_retriever()

    c
    rag_chain = (
        {
            "context": retriever | format_docs,
            "input": RunnablePassthrough(),
        }
        | retrieval_qa_prompt
        | chat
        | StrOutputParser()
    )

    
    docs = retriever.invoke(query)
    for doc in docs:
        doc.metadata.setdefault("source", "Unknown Source")

    
    result = {
        "input": query,
        "chat_history": chat_history,
        "context": docs,
        "answer": rag_chain.invoke({"input": query, "chat_history": chat_history}),
    }

    return result
