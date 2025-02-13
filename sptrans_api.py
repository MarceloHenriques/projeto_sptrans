import requests
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("Chave da API não encontrada. Verifique o arquivo .env.")

url = "http://api.olhovivo.sptrans.com.br/v2.1"
headers = {"Authorization": f"Bearer {API_KEY}"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print('Requisição realizada com sucesso!')
else:
    print(f"Erro na requisição: {response.status_code}")
