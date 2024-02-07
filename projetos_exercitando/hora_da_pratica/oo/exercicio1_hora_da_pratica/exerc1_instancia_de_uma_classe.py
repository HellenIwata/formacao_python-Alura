def executar_exercicios():
    class Restaurante:
        nome = ''
        categoria = ''
        ativo = False
    restaurante_praca = Restaurante()
    restaurante_praca.nome = 'Macarronada Bernadete'
    
    #1.Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
    restaurante_praca.categoria = 'Italiano'
    
    #2.Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.    
    nome_restaurante = restaurante_praca.nome
    
    #3. Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
    if restaurante_praca.ativo:
        print('Restaurante ativo')
    else:
        ('Hmm, o restaurante esta desativado :()')
        
    #4. Acesse o valor do atributo de classe categoria diretamente da classe Restaurante.
    categoria = restaurante_praca.categoria
    
    #5. Altere o valor do atributo nome para 'Bistrô'.
    restaurante_praca.nome = 'Bistrô'
    
    #6. Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
    restaurante_pizza = Restaurante()
    restaurante_pizza.nome = 'Pizza Place'
    restaurante_pizza.categoria = 'Fast Food'
    
    #7. Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
    if restaurante_pizza.categoria == 'Fast Food':
        print(f'a categoria deste restaurante é {restaurante_pizza.categoria}.')
    else:
        print(f'a categoria deste restaurante não é Fast Food')
    
    #8. Mude o estado da instância restaurante_pizza para ativo.
    restaurante_pizza.ativo = True
    
    #9. Imprima no console o nome e a categoria da instância restaurante_praca.
    print(f'o restaurante {restaurante_praca.nome} é vinculado a categoria {restaurante_praca.categoria}')
    
if __name__ == '__main__':
    executar_exercicios()