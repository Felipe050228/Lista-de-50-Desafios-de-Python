# Definição da classe Carro
class Carro:

    # Método construtor: executa quando o objeto é criado
    def __init__(self, nome_do_carro):
        # Atributo com o nome do carro
        self.nome_do_carro = nome_do_carro

        # Estados iniciais do carro
        self.ligado = False        # O carro começa desligado
        self.andando = False       # O carro começa parado
        self.combustivel = False   # O carro começa sem combustível

    # Método para ligar o carro
    def ligar(self):
        # Verifica se o carro ainda não está ligado
        if not self.ligado:
            self.ligado = True     # Muda o estado para ligado
            print('O carro está ligado\n')
        else:
            # Caso o carro já esteja ligado
            print('O carro já está ligado\n')

    # Método para desligar o carro
    def desligar(self):
        self.ligado = False        # Desliga o carro
        self.andando = False       # Para o carro automaticamente
        print('O carro está desligado\n')

    # Método para andar com o carro
    def andar(self):
        # Não pode andar se estiver desligado
        if not self.ligado:
            print('Não é possível andar, o carro está desligado\n')

        # Não pode andar se não tiver combustível
        elif not self.combustivel:
            print('Sem combustível, abasteça primeiro\n')

        # Se estiver ligado e com combustível
        else:
            self.andando = True    # O carro começa a andar
            print('O carro está andando\n')

    # Método para abastecer o carro
    def abastecer(self):
        self.combustivel = True    # Marca que agora há combustível
        print('O carro foi abastecido, boa viagem!\n')


# Cabeçalho visual
print('==' * 20)
print(' ' * 10, 'VAMOS ANDAR DE CARRO')
print('==' * 20)

# Criação do objeto carro
carro1 = Carro('Meu Carro')

# Pergunta ao usuário se quer ligar o carro
resposta = input(
    'Pressione ENTER para ligar o carro ou digite 000 para sair\n'
)

# Se o usuário digitar 000, o programa encerra
if resposta == '000':
    print('Então vamos deixar para outro dia')

# Caso contrário, liga o carro
else:
    carro1.ligar()

    # Pergunta se deseja abastecer
    resposta = input(
        'Pressione ENTER para abastecer ou digite 000 para não abastecer\n'
    )

    # Se não for 000, abastece o carro
    if resposta != '000':
        carro1.abastecer()

    # Pergunta se deseja andar
    resposta = input(
        'Pressione ENTER para andar ou digite 000 para ficar parado\n'
    )

    # Se não for 000, o carro anda
    if resposta != '000':
        carro1.andar()
