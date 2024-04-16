# Manipulação de Strings no Python

A manipulação de strings no Python envolve a aplicação de operações a uma string (texto) para obter informações relevantes para a aplicação.

Neste curso, abordaremos os seguintes tópicos:

1. Classe `str` e seus métodos básicos.
2. Princípios de orientação a objetos para a criação de uma classe própria responsável pela extração do valor dos parâmetros de uma URL.
3. Expressões regulares (regex) - ferramenta utilizada para identificar um determinado padrão dentro de um texto.
4. Métodos especiais do Python.

## Aula 1: Introdução e fatiamento de string

### Parâmetros em páginas da Internet
Quando navegamos na internet, frequentemente nos deparamos com URLs, que são endereços únicos para recursos na web. Uma URL geralmente consiste em duas partes principais: a base, que identifica o domínio ou site que estamos visitando, e os parâmetros, que são informações adicionais transmitidas para o servidor.

Os parâmetros em uma URL são essenciais para a comunicação entre o cliente (geralmente um navegador da web) e o servidor. Eles são separados do resto da URL por um ponto de interrogação (?) e podem conter uma variedade de informações, como consultas de pesquisa, identificadores de sessão, tokens de autenticação e muito mais.

Por exemplo, imaginemos que estamos construindo uma aplicação para o banco ByteBank que realiza conversões de moeda. A URL que nossa aplicação utiliza para consultar as taxas de câmbio pode ter a seguinte estrutura:
http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100

Nesta URL:
- `https://bytebank.com` é a base da URL, indicando o domínio do site.
- `/cambio` é o caminho específico no servidor onde a conversão de moeda é processada.
- `moedaOrigem=real`, `moedaDestino=dolar` e `quantidade=100` são os parâmetros que especificam os detalhes da conversão, como a moeda de origem, a moeda de destino e a quantidade a ser convertida.


### Fatiamento de Strings
Em Python, o fatiamento de strings é uma funcionalidade poderosa que nos permite extrair partes específicas de uma string com facilidade. Cada caractere em uma string possui uma posição associada, começando do índice 0.

Por exemplo, se tivermos a string `'abcd'`, podemos acessar diferentes partes dela usando a notação de fatiamento, como `texto[0:3]`, que retorna `'abc'`. Isso significa que estamos extraindo os caracteres desde o índice 0 até o índice 2 (o índice 3 não está incluso), resultando em `'abc'`.

O fatiamento de strings é uma técnica fundamental em Python, amplamente utilizada em tarefas como processamento de texto, análise de dados e manipulação de URLs.

Nesta aula, exploraremos detalhadamente como utilizar o fatiamento de strings para manipular e extrair informações importantes em nossos programas Python.

