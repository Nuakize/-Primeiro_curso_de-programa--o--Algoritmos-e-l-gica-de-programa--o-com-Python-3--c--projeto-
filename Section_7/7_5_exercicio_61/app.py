class Carro:
    def __init__(self, marca, valor, numero_portas, tanque):
        self.marca = marca
        self.valor = valor
        self.numero_portas = numero_portas
        self.tanque = tanque

    def abastecer(self, litros):
        if self.tanque >= 100:
            print("Tanque está cheio.")
        else:
            self.tanque += litros
            if self.tanque > 100:
                self.tanque = 100

    def dirigir(self, km):
        km_por_litro = 10
        self.tanque -= (km/km_por_litro)



carro = Carro("BMW", 2000000, 4, 80)

print(carro.marca)

carro.abastecer(100)

print(carro.tanque)

carro.dirigir(100)

print(carro.tanque)

carro.abastecer(10)

print(carro.tanque)