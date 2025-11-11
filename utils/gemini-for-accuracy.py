from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')

model = ChatGoogleGenerativeAI(
    model='gemini-2.0-flash',
    google_api_key="AIzaSyC-S_pMJfASJJmMFwFbMdVSZOuX4tmM4gM"
)

prompt=PromptTemplate(template="""
    You are an English fluency evaluator.
    Compare the following texts and respond
    Reference text {generated_text}  Spoken transcription  {spoken_text} Return 
        "fluency_score" from (0-100) and feedback  one-sentence feedback about fluency and improvements 
        of 30 -50 words having all the instruction for improvement and corrections and what to focus on and how to 
    """,
    input_variables=['generated_text','spoken_text'])

parser=StrOutputParser()

chain= prompt | model | parser 

def compare_text(generated_text,spoken_text):
    result=chain.invoke({'generated_text':generated_text,'spoken_text':spoken_text})

    return result