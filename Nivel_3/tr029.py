# Primeiro e segundo termos da sequência de Fibonacci
num1 = 0 
num2 = 1

# Função que calcula o n-ésimo termo da sequência de Fibonacci
def fib(n):
    # Se n for 0 ou 1, o próprio número já é o termo da sequência
    if n <= 1:
        print(n)

    # Reiniciando os valores dentro da função
    num1 = 0
    num2 = 1

    # Loop para calcular o termo n
    # Cada repetição calcula o próximo número da sequência
    for _ in range(n):
        num3 = num1 + num2  # Soma dos dois últimos termos
        num1 = num2         # Avança o termo anterior
        num2 = num3         # Atualiza o último termo

    # Mostra o n-ésimo termo calculado
    print(f'\033[1;32m{num1}\033[m')

# Mostra o primeiro termo (0) com cor amarela
print(f'\033[1;33m{num1}\033[m', end='/')

termo = 11  # Quantidade de termos a gerar

# Loop para exibir a sequência de Fibonacci
for i in range(termo):
    num3 = num1 + num2       # Calcula o próximo termo
    print(f'\033[1;33m{num2}\033[m', end='/')  # Mostra o termo atual
    num1 = num2              # Avança para o próximo termo
    num2 = num3              # Atualiza o último termo

print()  # Apenas quebra a linha

# Chama a função para calcular o 10º termo
fib(n=termo)
