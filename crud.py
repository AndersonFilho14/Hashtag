nome = input("Nome do usuario: ")
idade = input('idade, escreva somente numero ')
nacionalidade = input('Nacionalidade ')
resposta = ''
while resposta != "pausar":
    if int in nome:
        print('Refaça seu nome, tem um numero nele')

    input('Se quiser parar, digite "pausar"')
    
print(f'Seu nome é {nome}, tem idade {idade}, nascido na {nacionalidade}')

