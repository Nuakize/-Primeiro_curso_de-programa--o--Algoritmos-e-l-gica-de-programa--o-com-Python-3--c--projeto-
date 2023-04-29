conta_bancaria = float(359.56)

nova_quantia = float(input("Insira seu saldo na sua conta que atualmente está com R$359.56: "))

banco_total = conta_bancaria + nova_quantia

fatura_cartão = banco_total - 125.98

print("Com a fatura do cartão, sua conta estará com o saldo de %.2f" %fatura_cartão)