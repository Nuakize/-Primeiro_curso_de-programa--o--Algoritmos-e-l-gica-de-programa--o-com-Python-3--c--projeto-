class Mamifero:
    def __init__(self, patas, orelhas):
        self.patas = patas
        self.orelhas = orelhas

    def andar(self):
        print("O mamifero andou!")

class Cachorro(Mamifero):
    def __init__(self, patas, orelhas, cor_pelo):
        super().__init__(patas, orelhas)
        self.cor_pelo = cor_pelo

    def latir(self):
        print("Au Au!")

class Gato(Mamifero):
    def __init__(self, patas, orelhas, listras):
        super().__init__(patas, orelhas)
        self.listras = listras

    def miar(self):
        print("Miauuu!")

turca = Cachorro(4, 2, "Branca")
bartolomeu = Gato(4, 2, False)

turca.andar()
bartolomeu.andar()

turca.latir()
bartolomeu.miar()

print(turca.patas, turca.orelhas, turca.cor_pelo)
print(bartolomeu.patas, bartolomeu.orelhas, bartolomeu.listras)