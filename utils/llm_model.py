from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Get API key from environment
api_key = os.getenv('GOOGLE_API_KEY')

model = ChatGoogleGenerativeAI(
    model='gemini-2.0-flash',
    google_api_key="AIzaSyC-S_pMJfASJJmMFwFbMdVSZOuX4tmM4gM"
)

prompt = PromptTemplate(
    template="generate a detailed summary or story based on the {topic} , limit it arount {length} words",
    input_variables=['topic','length ']
)

parser = StrOutputParser()
chain = prompt | model | parser


def generate_text(topic,length):
    result = chain.invoke({'topic': topic,"length":length})
    return result

