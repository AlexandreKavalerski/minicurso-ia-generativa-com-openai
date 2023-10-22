from pydantic import BaseModel


class ProgramaCreate(BaseModel):
    descricao: str
    linguagem: str
