from pydantic import BaseModel


class TraducaoCreate(BaseModel):
    linguagem_origem: str
    linguagem_destino: str
    trecho_de_codigo: str
