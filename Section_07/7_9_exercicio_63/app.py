class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Poder(Pessoa):
    def __init__(self, nome, idade, poder):
        super().__init__(nome, idade)
        self.poder = poder

    def utilizar_poder(self):
        print("O herói utilizou sua %s" %self.poder)


kauan = Pessoa("Kauan", 18)

print(kauan.idade)

sapato = Poder("sapato", 77, "SAPATINA")

sapato.utilizar_poder()