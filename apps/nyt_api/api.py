import requests
import os
from dotenv import load_dotenv
from .translator import translate_this

load_dotenv()


def get_news():
    # Parâmetros para a requisição
    params = {
        'api-key': os.getenv('API_KEY')
    }

    # Fazendo a requisição
    response = requests.get(os.getenv('API_URL'), params=params)

    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Convertendo a resposta JSON para um dicionário
        dados = response.json()

        # Pegando os resultados das notícias
        noticias = dados.get('results', [])

        # Exibindo as notícias
        for i, noticia in enumerate(noticias[:5]):
            print(f"Notícia {i+1}:")
            print(f"Título: {translate_this(noticia['title'])}")
            print(f"Resumo: {noticia['abstract']}")
            print(f"Link: {noticia['url']}\n")

    else:
        print(f"Erro ao obter notícias: {response.status_code}")
