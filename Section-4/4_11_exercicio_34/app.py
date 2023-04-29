n = int(input("Digite um número: "))

divisoes = 0

contador = n

while contador > 0:

    if n % contador == 0:
        divisoes = divisoes + 1

    contador = contador - 1

if divisoes == 2:
    print("O número %d é primo!" % n)

else:
    print("O número %d não é primo!" % n)
