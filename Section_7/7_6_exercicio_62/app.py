class Banco:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def trasnferencia(self, outra_conta, valor):
        self.saldo -= valor
        outra_conta.saldo += valor

conta_kauan = Banco('Kauan', 1000)

print(conta_kauan.nome)

conta_kauan.deposito(1000)

print(conta_kauan.saldo)

conta_kauan.saque(1500)

print(conta_kauan.saldo)

conta_maria = Banco("Maria", 100)

conta_kauan.trasnferencia(conta_maria, 200)

print(conta_maria.saldo)

print(conta_kauan.saldo)