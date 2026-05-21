# assistente virtual que gera uma explicação e com o sistema de memoria.


import os

from dotenv                        import load_dotenv
from langchain_groq                import ChatGroq
from langchain_core.prompts        import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages       import HumanMessage, AIMessage, SystemMessage


load_dotenv()


modelo = ChatGroq(
    api_key = os.environ.get("GROQ_API_KEY"),
    model = "openai/gpt-oss-120b",
    temperature = 0.7,
    max_tokens = 1000,
)

historico = [
    SystemMessage(content = "Você é um Tutor de programação em Python."),
]

perguntas =[
    "O que é uma lista em Python?",
    "Como eu adiciono um item nela?",
]

for pergunta in perguntas:
    historico.append(HumanMessage(content=pergunta))
    resposta = modelo.invoke(historico)
    historico.append(AIMessage(content=resposta.content))

    print(f"Aluno: {pergunta}")
    print(f"IA: {resposta.content}\n")