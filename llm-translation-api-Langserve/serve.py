
## ------------- IMPORT ALL THE LIBRARIES --------------


from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os 
from dotenv import load_dotenv
from langserve import add_routes
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

from langchain_openai import ChatOpenAI


# ---------------- Model Is created ---------------

from langchain_groq import ChatGroq
model = ChatGroq(model="llama-3.3-70b-versatile",groq_api_key = groq_api_key)

#----------------- Create Prompt Template --------------

system_template = "Translate the following into {language}:"

prompt = ChatPromptTemplate.from_messages(
    [("system" , system_template) ,
    ("user","{text}")]
)


#-------------------Parser -------------------
parser = StrOutputParser()

# ---------------- LCEL CHAIN ---------------
chain = prompt|model|parser



#---------- App Defination----------
app = FastAPI(title="Langchain Server",
              Version = "1.0",
              Description = "A simple API server using Langchain runnable interfaces")

# -------------Adding chain routes ----------
add_routes(
    app,
    chain,
    path="/chain"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host = "127.0.0.1" , port = 8000)

