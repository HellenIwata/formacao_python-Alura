from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint que exibi uma mensagem de 'olá mundo' para o usuário
    '''
    return{'Hello':'World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante:str = Query(None)):
    '''
    Endpoint que lista todos os restaurantes ou busca por um restaurante específico pelo nome.\n
    '''
    
    url ='https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None: #Se nenhuma informação do restaurante for passado
            return {'Dados': dados_json}
        
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:               
                dados_restaurante.append({
                'ITEM': item['Item'], 
                'PRICE': item['price'], 
                'DESCRIPTION': item['description']})
        return{'Restaurante':restaurante, 'Cardapio': dados_restaurante}
    else:
        return{'Erro':f"{response.status_code} - {response.text}"}
    

    