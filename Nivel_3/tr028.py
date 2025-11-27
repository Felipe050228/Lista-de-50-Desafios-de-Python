from random import choice

# Lista com letras minúsculas, maiúsculas e números que serão usadas para montar a senha
lista_de_caracteris =  [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"
]

# Função que gera e exibe uma senha aleatória
def senhas_aleatorias(caracterís):
    print('==='*10)   
    print('     SENHA:', end=' ')
    
    # Laço para gerar 10 caracteres aleatórios
    for i in range(1, 11):
        # choice escolhe 1 elemento aleatório da lista
        print(f'\033[1;33m{choice(caracterís)}\033[m', end='')
    
    print()  # Quebra de linha após a senha
    print('==='*10)

# Chamada da função passando a lista de caracteres
senhas_aleatorias(caracterís = lista_de_caracteris)
