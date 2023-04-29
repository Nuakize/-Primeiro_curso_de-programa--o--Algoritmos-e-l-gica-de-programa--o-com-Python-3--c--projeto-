class Pessoa:
    def falar(self):
        print("Olá pessoal!")

class Kauan(Pessoa):
    def falar(self):
        print("Olá pessoal, eu sou o Kauan!")

class Roberto(Pessoa):
    pass


kauan = Kauan()

kauan.falar()

roberto = Roberto()

roberto.falar