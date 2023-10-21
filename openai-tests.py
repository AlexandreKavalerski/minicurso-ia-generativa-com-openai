import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "gpt-3.5-turbo"


def poema():
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "Você é um assistente poeta, muito habilidoso em explicar conceitos complexos de computação com criatividade e talento",
            },
            {
                "role": "user",
                "content": "Escreva um poema que explique o conceito de recursão em programação",
            },
        ],
    )

    print(completion.choices[0].message.content)


def rude():
    setup_assistente = {
        "role": "system",
        "content": "Você é um assistente que responde de maneira MUITO rude e com ironia e sarcasmo",
    }
    comando = ""
    mensagens = [setup_assistente]

    while comando != "sair":
        comando = input("-")
        mensagens.append({"role": "user", "content": comando})

        completion = client.chat.completions.create(model=model, messages=mensagens)

        saida = completion.choices[0].message.content
        mensagens.append({"role": "assistant", "content": saida})
        print(saida)


if __name__ == "__main__":
    print("em execução...")
    # poema()
    # rude()
