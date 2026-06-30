from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
from langchain_google_genai import ChatGoogleGenerativeAI

def main():
    #test google generative ai model
    model = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0)
    response = model.invoke("Setup Done")
    print(f"Response from Google:{response}")


if __name__ == "__main__":
    main()
