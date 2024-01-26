class ContaBancaria:
    #1. Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

    #2. Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
    def __str__(self):
        return f'{self.titular} | R$ {self.saldo} | {self._ativo}'
    
    #3. Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = not conta._ativo
        
#Print do tópico 2
conta1 = ContaBancaria(titular='Hellen Cristina', saldo=5.95)
conta2 = ContaBancaria(titular='Dhara Victoria', saldo=105.95)
print(conta1)
print(conta2)

#Print do tópico 3
conta3 = ContaBancaria(titular='Celina', saldo=1005.95)
print(f'validação antes de ativar a conta. A conta está ativa? {conta3._ativo}')
ContaBancaria.ativar_conta(conta3)
print(f'validação após ativação de conta. A conta está ativa? {conta3._ativo}')

#4. Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.
class RefatorandoContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
        
    @property
    def titular(self):
        return self._titular
    
    def saldo(self):
        return self._saldo
    
    def ativo(self):
        return self._ativo
    
#5. Crie uma instância da classe e imprima o valor da propriedade titular.
conta4 = RefatorandoContaBancaria(titular='Cristina Santos', saldo=255.00)
print(f'O titular da 4º conta é: {conta4.titular}')

#6. Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
class ClienteBanco:
    def __init__(self, nome, ano_nascimento, cpf, endereco, estado_civil):
        self.nome = nome
        self.ano_nascimento = ano_nascimento
        self._cpf = cpf
        self.endereco = endereco
        self.estado_civil = estado_civil

#7. Crie um método de classe para a conta ClienteBanco'.
    @classmethod
    def criar_conta(cls, titular, conta, tipo_de_conta, limite_inicial):
        conta = RefatorandoContaBancaria(titular, conta, tipo_de_conta, limite_inicial)
        return conta

#Instâncias do tópico 6
cliente1 = ClienteBanco(nome='Josué Nascimento', ano_nascimento= 1990, cpf= 12345678900, endereco='Rua Bras, 188', estado_civil='Viúvo')
cliente2 = ClienteBanco(nome='Maria Clara', ano_nascimento= 2003, cpf= 98765432188, endereco='Rua jardim antonieta, 191', estado_civil='Solteira')
cliente3 = ClienteBanco(nome='Antonio Carlos', ano_nascimento= 1954, cpf= 10230569865, endereco='Rua São Paulo, 88', estado_civil='Casado')
