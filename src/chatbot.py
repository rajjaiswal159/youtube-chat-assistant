# Import Gemini chat model
from langchain_google_genai import ChatGoogleGenerativeAI

# Import prompt template
from langchain_core.prompts import ChatPromptTemplate

# Import environment variable loader
from dotenv import load_dotenv

# Load .env variables
load_dotenv()


# Generate answer using retrieved context
def ask_question(vector_store, question):

    # Retrieve relevant chunks
    retriever = vector_store.as_retriever(
        search_kwargs={"k": 2}
    )

    docs = retriever.invoke(question)

    # Combine retrieved chunks
    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    # Create prompt template
    prompt = ChatPromptTemplate.from_template(
        """
        Answer the question using ONLY the provided context.

        Context:
        {context}

        Question:
        {question}

        If the answer is not present in the context,
        say "I could not find that information in the video."

        Answer:
        """
    )

    # Initialize Gemini model
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash"
    )

    # Create final prompt
    formatted_prompt = prompt.format(
        context=context,
        question=question
    )

    # Generate response
    response = llm.invoke(formatted_prompt)

    # Return answer text
    return response.content