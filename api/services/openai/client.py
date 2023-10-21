import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "gpt-3.5-turbo"


def identificar_linguagem_codigo(trecho_de_codigo=""):
    # TODO: criar metodo
    pass


def criar_programa(descricao_programa=""):
    # TODO: criar metodo
    pass


def converter_codigos(linguagem_origem="", linguagem_destino="python", codigo=""):
    instrucoes = """Você é um especialista em engenharia de software. Sabe muito bem como modificar um código em qualquer linguagem de programação para qualquer outra de forma objetiva. Você receberá uma entrada no seguinte formato: 
    converta
    ORIGEM: <nome_da_lingugagem>
    DESTINO: <nome_da_linguagem>
    CODIGO: <trecho_de_codigo_para_converter>
    Converta o código escrito na linguagem origem para a linguagem destino.
    Responda apenas o resultado do trecho de código convertido para a linguagem indicada. 
    Não comente os trechos de código.
    """

    setup_assistente = {
        "role": "system",
        "content": instrucoes,
    }

    instrucao = f"""converta
    ORIGEM: {linguagem_origem}
    DESTINO: {linguagem_destino}
    CODIGO: {codigo}
    """

    completion = client.chat.completions.create(
        model=model,
        messages=[
            setup_assistente,
            {
                "role": "user",
                "content": instrucao,
            },
        ],
    )

    return completion.choices[0].message.content
