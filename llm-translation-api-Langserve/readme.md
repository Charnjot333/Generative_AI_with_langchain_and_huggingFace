# LangChain Translation API
<img src="assets/Langserve_1.png" width="700">

A simple multilingual translation API built using **LangChain**, **FastAPI**, **LangServe**, and **Groq's Llama 3.3-70B** model.

<img src="assets/Langserve_2.png" width="700">

## What I Learned

- **LangChain** – A framework for building applications powered by Large Language Models (LLMs).
- **Prompt Templates** – Create reusable and dynamic prompts by inserting user inputs into predefined templates.
- **LCEL (LangChain Expression Language)** – Chain multiple LangChain components together using a simple pipeline (`|`) syntax.
- **StrOutputParser** – Converts the model's response into a plain string for easy use.
- **FastAPI** – Build and expose the LangChain application as a REST API.
- **LangServe** – Deploy LangChain chains as API endpoints with minimal configuration.
- **Groq Integration** – Connect LangChain to Groq-hosted open-source LLMs for fast inference.
- **Environment Variables (.env)** – Securely store and access API keys without hardcoding them in the source code.

## Tech Stack

- Python
- LangChain
- FastAPI
- LangServe
- Groq
- Llama 3.3-70B
- Uvicorn
- python-dotenv

## Run the Project

```bash
pip install -r requirements.txt
python serve.py
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
```

## Future Learning

- Document Loaders
- Text Splitters
- Embeddings
- Vector Databases
- Retrievers
- Retrieval-Augmented Generation (RAG)
- Memory
- Agents
- Tools
- LangSmith
