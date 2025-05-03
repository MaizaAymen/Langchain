import os
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

os.environ["GROQ_API_KEY"] = "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"

llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0.3,
    max_tokens=500,
)

prompt_template = PromptTemplate.from_template(
    "List {n} cooking/meal titles for {cuisine} cuisine (name only)."
)

chain = prompt_template | llm

def main():
    print("🍝 Meal Generator AI 🍱")
    cuisine = input("Enter a cuisine (e.g., Italian, Indian): ")
    n = input("How many meal titles? ")

    try:
        n = int(n)
        response = chain.invoke({"n": n, "cuisine": cuisine})
        print("\nGenerated Meal Titles:")
        print(response.content)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
