lista = [1,2,3,4,5]

elemento = int(input("Digite um número de 1 a 5: "))

encontrado = False

for n in lista:
    if n == elemento:
        print("O número digitado está na lista (%d)!!!" %n)
        encontrado = True


if encontrado == False:
    print("O número digitado não está na lista (%d)!!!" %elemento)