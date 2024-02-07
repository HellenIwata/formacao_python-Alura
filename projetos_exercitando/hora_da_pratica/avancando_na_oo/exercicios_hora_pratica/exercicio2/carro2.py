# 3. Crie uma nova classe chamada Carro que herda da classe Veiculo.
from exercicio2.veiculo2 import VeiculoAvancado
# 4. No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.
class CarroAvancado(VeiculoAvancado):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self._cor = cor
        
    def __str__(self):
        return f'{self._marca} | {self._modelo} | {self._cor} '
# 5. Em um arquivo chamado main.py, importe a classe Carro.
# 6. No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.