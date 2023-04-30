class Carro:
    def __init__(self, portas, motor, teto_solar, marca, preco):
        self.portas = portas
        self.motor = motor
        self.teto_solar = teto_solar
        self.marca = marca
        self.preco = preco

carro = Carro(4, 1, 0, "Chevrolet", 100000.00)

if carro.motor == 1:
    print("O carro tem %d portas; %d motor; %d teto solar; é da marca %s; custou R$%.2f" %(carro.portas, carro.motor, carro.teto_solar, carro.marca, carro.preco))


carro2 = Carro(2, 1, 1, "Fiat", 50000.00)

if carro2.motor == 1:
    print("O carro tem %d portas; %d motor; %d teto solar; é da marca %s; custou R$%.2f" %(carro2.portas, carro2.motor, carro2.teto_solar, carro2.marca, carro2.preco))