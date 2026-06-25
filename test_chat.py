from src.vectorstore import load_vector_store
from src.chatbot import ask_question

# Load FAISS index
vector_store = load_vector_store()

while True:

    # Take user question
    question = input("\nAsk a question: ")

    # Exit condition
    if question.lower() == "exit":
        break

    # Get answer
    answer = ask_question(
        vector_store,
        question
    )

    # Print answer
    print("\nAnswer:")
    print(answer)