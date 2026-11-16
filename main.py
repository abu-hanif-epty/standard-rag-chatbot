from app.generation.chain import (
    create_rag_pipeline,
    get_rag_response
)


def main():

    print("=" * 45)
    print("       STANDARD RAG CHATBOT")
    print("=" * 45)

    # Initialize only once
    print("Initializing RAG application...")

    retriever, chain = create_rag_pipeline()

    print("RAG application ready!")
    print("Type 'exit' to quit.")

    while True:

        question = input("\nYou: ").strip()

        if question.lower() == "exit":
            print("Goodbye!")
            break

        if not question:
            print("Please enter a question.")
            continue

        try:

            response = get_rag_response(
                question,
                retriever,
                chain
            )

            print(f"\nAssistant: {response}")

        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()