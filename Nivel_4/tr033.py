
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo_atual = saldo_inicial
        print(f'Conta para {self.titular} criada com sucesso!')

    def depositar(self, valor):
        if valor > 0:
            self.saldo_atual += valor
            print(f'Depósito de R${valor:.2f} feito com sucesso.')
        else:
            print('ERRO| O valor do depósito deve ser positivo.')
        self.saldo()

    def sacar(self, valor):
        if valor > self.saldo_atual:
            print(f'ERRO| Saldo insuficiente. Você tem R${self.saldo_atual:.2f} disponíveis.')
        elif valor <= 0:
            print('ERRO| O valor do saque deve ser positivo.')
        else:
            self.saldo_atual -= valor
            print(f'Saque de R${valor:.2f} feito com sucesso.')
        self.saldo()

    def saldo(self):
        # Acessando atributos diretamente
        print('=='*15)
        print(f"Titular: {self.titular}")
        print(f"Saldo Atual: R${self.saldo_atual:.2f}")
        print('=='*15)

def main():
    print('=='*10)
    print(" bem vindo ao \n bencodev")
    print('=='*10)
    print('vamos criar uma conta para você')

    nome = input('Digite seu nome: ').capitalize()
    saldo_inicial = 0.0

    while True:
        try:
            saldo_input = input('Agora digite seu saldo inicial (ou Enter para 0): ')
            if saldo_input == "":
                break
            saldo_inicial = float(saldo_input)
            if saldo_inicial < 0:
                print('ERRO| O saldo inicial não pode ser negativo.')
                continue
            break
        except ValueError:
            print('ERRO| Digite um valor numérico válido para o saldo.')
    
    # Cria a instância da conta bancária
    conta = ContaBancaria(nome, saldo_inicial)

    # Loop principal de operações que não quebra após 1 operação
    while True:
        print("\nO que deseja fazer?")
        opcoes = input('[1] Depositar\n[2] Sacar\n[3] Ver Saldo\n[4] Sair\n: ')

        if opcoes == "1":
            while True:
                try:
                    mony = float(input('Quanto deseja depositar: R$'))
                    conta.depositar(valor=mony)
                    break
                except ValueError:
                    print('ERRO| Digite um valor numérico válido.')
        
        elif opcoes == "2":
            while True:
                try:
                    mony = float(input('Quanto deseja sacar: R$'))
                    conta.sacar(valor=mony)
                    break
                except ValueError:
                    print('ERRO| Digite um valor numérico válido.')

        elif opcoes == "3":
            conta.saldo()
        
        elif opcoes == "4":
            print('Saindo do sistema.')
            break
        
        else:
            print('ERRO| Digite uma opção válida (1, 2, 3 ou 4).')

    print('VOLTE SEMPRE')

# Garante que o script seja executado apenas quando rodado diretamente
if __name__ == "__main__":
    main()

