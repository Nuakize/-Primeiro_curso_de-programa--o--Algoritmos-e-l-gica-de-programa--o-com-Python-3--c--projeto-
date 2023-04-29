class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

kauan = Pessoa("Kauan", 18, "Programador")

print(kauan.nome)
print(kauan.idade)
print(kauan.profissao)

if kauan.nome == "Kauan":
    print("Olá Kauan")

nome = kauan.nome

print(nome)