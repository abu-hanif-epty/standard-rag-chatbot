from app.generation.chain import get_rag_response

question = input("Ask a question: ")

response = get_rag_response(question)

print("\nAnswer:")
print(response)