from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
import requests, json

url ='https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
print(response)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
            
        dados_restaurante[nome_do_restaurante].append({
            'ITEM': item['Item'], 
            'PRICE': item['price'], 
            'DESCRIPTION': item['description']})
else:
    print(f'o erro foi: {response.status_code}')
    
for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo, 'w') as arquivo_restaurante: # With open: permite manipular os arquivos dentro da aplicação
        json.dump(dados, arquivo_restaurante, indent=4)


""" restaurante_sushi_iwata = Restaurante('Iwata Sushi', 'Japonês')
bebida_suco = Bebida('Coca-Cola', 8.00, 'M')
prato_yakissoba = Prato('Yakissoba tradicional', 45.50, 'Yakissoba tradicional com carne, frango e legumes')

# restaurante_jorge_boteco = Restaurante('Boteco do Jorge','Brasileira')
# restaurante_muy_loca = Restaurante('Muy Loca', 'Mexicana')

def main():
    restaurante_sushi_iwata.adicionar_ao_cardapio(prato_yakissoba)
    restaurante_sushi_iwata.adicionar_ao_cardapio(bebida_suco)
    
    restaurante_sushi_iwata.listar_cardapio 

if __name__ == '__main__':
    main() """