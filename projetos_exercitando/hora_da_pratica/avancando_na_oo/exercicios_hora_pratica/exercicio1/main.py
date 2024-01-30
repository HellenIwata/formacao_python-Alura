#7. Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.

#8. Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.
from carro import Carro
from moto import Moto

#Instanciando a classe Carro:
carro1 = Carro('Toyota', 'Corolla', 4)
carro2 = Carro('Chevrolet', 'Celta', 2)
carro3 = Carro('Fiat', 'Uno', 2)

#Instanciando a classe Moto:
moto1 = Moto('Honda', 'CG-160')
moto2 = Moto('Yamaha', 'Fazer-250')
moto3 = Moto('BMW', 'G310R')

#9. Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.
print(carro1)
print(carro2)
print(carro3)
print(moto1)
print(moto2)
print(moto3)