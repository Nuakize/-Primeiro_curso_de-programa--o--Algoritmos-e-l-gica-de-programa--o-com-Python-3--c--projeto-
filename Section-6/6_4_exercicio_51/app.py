def menor_maior_10(numero):
    resultado = ""

    if numero == 10:
        resultado = "Exato 10."
    if numero > 10:
        resultado = "Maior que 10."
    if numero < 10:
        resultado = "Menor que 10."
    return resultado

a = 10
b = 20
c = 0

resp_a = menor_maior_10(a)
resp_b = menor_maior_10(b)
resp_c = menor_maior_10(c)

print(resp_a)
print(resp_b)
print(resp_c)
    