
# assistente virtual que gera uma explicação


import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


modelo = ChatGroq(
    api_key = os.environ.get("GROQ_API_KEY"),
    model = "openai/gpt-oss-120b",
    temperature = 0.7,
    max_tokens = 1000,
)

prompt = ChatPromptTemplate.from_messages([
    ("system","você e um assistente educacional do SENAI. Responda de forma clara e didatica."),
    ("human","Explique em 5 linhas o que é: {topico}"),
])

chain = prompt | modelo | StrOutputParser()

topicos = ["Inteligencia Artificial", "Machine Learning", "Redes Neurais "]

for topico in topicos:
    print(f"\nTópico: {topico}")
    print("-" * 40)
    resposta = chain.invoke({"topico": topico })
    print(resposta)