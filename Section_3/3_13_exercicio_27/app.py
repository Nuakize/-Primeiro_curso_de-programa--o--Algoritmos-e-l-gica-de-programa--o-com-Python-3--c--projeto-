renda = float(input("Digite sua renda mensal para liberar o limite do cartão de crédito: "))

if renda <= 2000:
    print("R$1000.00 de limite do cartão.")
elif renda <= 4000:
    print("R$2000.00 de limite do cartão.")
elif renda <= 10000:
    print("R$3000.00 de limite do cartão")
else:
    print("Contate o gerente.")