url = 'http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
print(url)

# Fatiamento
url = 'http://bytebank.com/cambio?moedaOrigem=real'
print(f'URL padrão: {url}')

url_base = url[0:26]
print(f'URL Base: {url_base}') 

url_parametro= url[27:45]
print(f'URL parametro: {url_parametro} ')
