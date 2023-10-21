from typing import Union
from fastapi import FastAPI

from api.schemas.traducao import TraducaoCreate
from api.services.openai import client as openai

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/traduzir/")
def traduzir_codigos(traducao: TraducaoCreate):
    """
    Informe linguagens de origem e destino e o trecho de código.
    O sistema irá responder com a "tradução" do código para a linguagem desejada.
    """
    resultado = openai.converter_codigos(
        linguagem_origem=traducao.linguagem_origem,
        linguagem_destino=traducao.linguagem_destino,
        codigo=traducao.trecho_de_codigo,
    )
    return resultado
