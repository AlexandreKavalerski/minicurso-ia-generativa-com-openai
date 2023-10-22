from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from api.schemas.traducao import TraducaoCreate
from api.schemas.programa import ProgramaCreate
from api.services.openai import client as openai

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/traducao/")
def traduzir_codigos(traducao: TraducaoCreate):
    """
    Informe linguagens de origem e destino e o trecho de código.
    O resultado é a "tradução" do código para a linguagem desejada.
    """
    resultado = openai.converter_codigos(
        linguagem_origem=traducao.linguagem_origem,
        linguagem_destino=traducao.linguagem_destino,
        codigo=traducao.trecho_de_codigo,
    )
    return resultado


@app.post("/programa/")
def criar_programa(programa: ProgramaCreate):
    """
    Informe uma descrição e a linguagem com a qual o programa deverá ser criado.
    O resultado é o código comentado.
    """
    resultado = openai.criar_programa(
        descricao=programa.descricao,
        linguagem=programa.linguagem,
    )
    return resultado
