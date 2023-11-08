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


def transcribe(file_path: str):
    import whisper

    whisper_model = whisper.load_model("small")
    # model = whisper.load_model("small", fp16=False, language="portuguese")

    result = whisper_model.transcribe(
        file_path,
    )
    content = result.get("text")
    print(content)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Você é um assistente tradutor especialista em síntese de conteúdos técnicos em computação",
            },
            {
                "role": "user",
                "content": f"Resuma do que se trata esse conteúdo: {content}",
            },
        ],
    )
    print(completion.choices[0].message.content)


def to_image(prompt="a white siamese cat"):
    from io import BytesIO
    from PIL import Image
    import requests

    response = client.images.generate(prompt=prompt)

    img_from_url = requests.get(response.data[0].url)

    image = Image.open(BytesIO(img_from_url.content))
    image.save("result.png")


if __name__ == "__main__":
    print("em execução...")
    # poema()
    # rude()
    # to_image()
    # transcribe("files/v2.mp4")
