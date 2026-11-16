from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from app.config import GROQ_API_KEY
from app.retrieval.retriever import get_retriever

def create_rag_chain():

    llm = ChatGroq(
        model="openai/gpt-oss-120b",  # or "openai/gpt-oss-20b" / "qwen/qwen3.8-27b"
        api_key=GROQ_API_KEY,
        temperature=0
    )
    prompt = ChatPromptTemplate.from_template("""
    You are a helpful AI assistant.

    Answer the question using ONLY the provided context.

    If the answer is not available in the context,
    say: "I don't know based on the provided documents."

    Context:
    {context}

    Question:
    {question}

    Answer:
    """)

    return prompt | llm | StrOutputParser()

    # return chain



def create_rag_pipeline():

    retriever = get_retriever()
    chain = create_rag_chain()

    return retriever, chain


def get_rag_response(question, retriever, chain):

    documents = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in documents
    )

    response = chain.invoke({
        "context": context,
        "question": question
    })

    return response