import requests
from requests.auth import HTTPBasicAuth

def authenticate_user(username, password):
    # URL da API
    api_url = "https://data.iprod.woodmac.com/query-internal/anp/all/odata"
    
    # Realizando a requisição com autenticação básica
    response = requests.get(api_url, auth=HTTPBasicAuth(username, password))
    
    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        return {"status_code": 200, "data": response.json()}  # Retorna os dados da resposta da API com status
    else:
        # Se falhar na autenticação, retorna um dicionário com status e mensagem de erro
        return {"status_code": response.status_code, "error": response.json()}
