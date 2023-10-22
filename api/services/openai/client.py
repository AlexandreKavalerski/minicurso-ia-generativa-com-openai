import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "gpt-3.5-turbo"


def _get_assistente(instrucoes: str):
    return {
        "role": "system",
        "content": instrucoes,
    }


def _get_completion_result(assistente: str, comando: str):
    setup_assistente = _get_assistente(assistente)

    completion = client.chat.completions.create(
        model=model,
        messages=[
            setup_assistente,
            {
                "role": "user",
                "content": comando,
            },
        ],
    )

    return completion.choices[0].message.content


def identificar_linguagem_codigo():
    # TODO: criar código
    pass


def criar_programa(descricao="", linguagem=""):
    instrucao_assistente = """Você é um especialista em engenharia de software. Sabe muito bem como criar um código em qualquer linguagem de programação de forma objetiva. Você receberá uma entrada no seguinte formato: 
    escreva um programa
    DESCRICAO: <descricao_do_programa>
    LINGUAGEM: <nome_da_linguagem>
    Escreva o código na linguagem definida.
    Responda apenas o resultado do trecho de código que atenda à solicitação. 
    Inclua comentários no código sempre que necessário - associe aos requisitos da DESCRICAO. Não inclua nenhum outro comentário fora do código.
    Retorne apenas o código no formato: ```linguagem CODIGO ```
    """

    comando = f"""escreva um programa
    DESCRICAO: {descricao}
    LINGUAGEM: {linguagem}
    """

    return _get_completion_result(assistente=instrucao_assistente, comando=comando)


def converter_codigos(linguagem_origem="", linguagem_destino="python", codigo=""):
    instrucao_assistente = """Você é um especialista em engenharia de software. Sabe muito bem como modificar um código em qualquer linguagem de programação para qualquer outra de forma objetiva. Você receberá uma entrada no seguinte formato: 
    converta
    ORIGEM: <nome_da_lingugagem>
    DESTINO: <nome_da_linguagem>
    CODIGO: <trecho_de_codigo_para_converter>
    Converta o código escrito na linguagem origem para a linguagem destino.
    Responda apenas o resultado do trecho de código convertido para a linguagem indicada. 
    Não comente os trechos de código.
    """

    comando = f"""converta
    ORIGEM: {linguagem_origem}
    DESTINO: {linguagem_destino}
    CODIGO: {codigo}
    """

    return _get_completion_result(assistente=instrucao_assistente, comando=comando)
