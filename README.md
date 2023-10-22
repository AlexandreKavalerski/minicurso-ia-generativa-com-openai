# Minicurso de Inteligência Artificial Generativa com OpenAI

Repositório do Minicurso de IA Generativa com API OpenAI ministrado por [Alexandre Kavalerski](https://www.kavalerski.com/) no ENCOINFO (https://ulbra-to.br/encoinfo). 
Este minicurso tem como objetivo instigar a geração de ideias para utilizar a inteligência artificial generativa na resolução de desafios e no desenvolvimento de soluções com potencial inovador.

## Tecnologias Utilizadas

O projeto utiliza as seguintes tecnologias:

- **Python**: Python é a linguagem de programação que vamos utilizar para escrever nossos códigos. Você pode instalar o Python a partir do [site oficial](https://www.python.org/downloads/).

- **API da OpenAI**: A OpenAI é uma empresa focada em pesquisa e desenvolvimento de IA. Vamos utilizar algumas soluções da API que dá acesso aos modelos de linguagem natural. Para utilizar a API, você deve gerar uma chave de API acessando o [link aqui](https://platform.openai.com/account/api-keys). 
> Nesse projeto estamos utilizando a versão beta da lib Python que "encapsula" algumas chamadas à API. Para mais detalhes, veja o [repositório da lib](https://github.com/openai/openai-python).

- **FastAPI**: FastAPI é um framework em Python para construir aplicações RESTful de forma rápida e seguindo os padrões modernos de desenvolvimento. Vamos usar FastAPI para construir uma API REST com as funcionalidades que iremos desenvolver.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado o Python e de ter gerado sua chave de API da OpenAI. Caso contrário, siga os passos descritos nas seções acima.

## Como Iniciar

1. Clone este repositório:

```bash
git clone https://github.com/AlexandreKavalerski/minicurso-ia-generativa-com-openai.git
```

2. Acesse a pasta do projeto:
```bash
cd minicurso-ia-generativa-com-openai
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Configure a chave de API da OpenAI:
>Crie um arquivo .env na raiz do projeto e adicione sua chave de API da OpenAI da seguinte forma:

```bash
OPENAI_API_KEY=SUA_CHAVE_DE_API_AQUI
```
5. Inicie o servidor FastAPI:
```bash
uvicorn api.main:app --reload

ou 

make up_api
```

6. Inicie o servidor do Client:
```bash
make up_client
```

7. Acesse o cliente em http://localhost:8080 e a documentação da API em http://localhost:8000/docs para começar a interagir com as funcionalidades desenvolvidas.

## Contribuições
Fique à vontade para contribuir com este projeto abrindo issues, propondo melhorias ou enviando pull requests. Sua colaboração é bem-vinda!

## Licença
Este projeto é distribuído sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

## Minicurso de Inteligência Artificial Generativa com OpenAI

Desenvolvido por [Alexandre Kavalerski](https://www.kavalerski.com/)