class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome.title()
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'

    @property
    def saudacao(self):
        return f'Ooi, me chamo {self.nome}, e trabalho como {self.profissao}' if self.profissao else f'Ooi, me chamo {self.nome}, e atualmente não trabalho ou preferi não informar.'
    
    def aniversario(self):
        self.idade += 1

    

pessoa1 = Pessoa(nome='hellen Cristina', idade=23, profissao='Analista de TI júnior') 
pessoa2 = Pessoa(nome='João Pedro', idade=25, profissao='Desenvolvedor Front-end júnior') 
pessoa3 = Pessoa(nome='Karine', idade=26) 


print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

pessoa1.aniversario()
pessoa2.aniversario()
pessoa3.aniversario()

print("Validação após aniversário:")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)
