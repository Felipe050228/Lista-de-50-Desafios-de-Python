# Importa a função randint, que permite gerar números inteiros aleatórios
from random import randint 

# Define uma função chamada "gerador", que recebe o nome de um arquivo como parâmetro
def gerador(nome_do_arquivo):
    try:
        # Abre (ou cria) o arquivo no modo de escrita ('w')
        # O 'with' garante que o arquivo será fechado automaticamente depois do uso
        with open(nome_do_arquivo, 'w') as arquivo:
            
            # Loop que vai de 1 até 8 (gera 8 números)
            for i in range(1, 9):
                
                # Gera um número aleatório entre 1 e 10
                numeros_escolhidos = randint(1, 10)
                
                # Escreve o número dentro do arquivo, convertendo para string
                arquivo.write(str(numeros_escolhidos) + "")
        
        # Mensagem exibida quando termina tudo sem erros
        print(f"Foram gerados 8 números e salvos no arquivo: {nome_do_arquivo}")

    except:
        # Caso aconteça algum erro ao salvar o arquivo (ex.: nome inválido)
        print(f"Erro ao salvar o arquivo: {nome_do_arquivo}")

# Pede ao usuário um nome para o arquivo que será criado
nome_do_meu_arquivo = input('Dê um nome ao seu arquivo: ')

# Chama a função passando o nome informado
gerador(nome_do_arquivo = nome_do_meu_arquivo)
