class Animal:
    def __init__(self,nome,raca):
        self.nome = nome
        self.raca = raca
        

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, raca)

    def apresentar (self):
        print(f'\n{self.nome} é da raça {self.raca}')
        print(f'{self.nome}: Au au!\n')


class Gato(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, raca)

    def apresentar (self):
        print(f'\no meu gato {self.nome} é da raça {self.raca}')
        print(f'{self.nome}: Miau!\n')


cachorro1 = Cachorro(nome='hulk',raca='pitbull') 
cachorro1.apresentar()
gato1 = Gato(nome='pricesa',raca='cianes')
gato1.apresentar()