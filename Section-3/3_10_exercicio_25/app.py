numero = int(input("Insira um número: "))

if numero >= 10:

    if numero < 20:
        print("Número menor que 20")
        print(numero * 2)
    else:
        print("Número maior que 20")
        print(numero * 5)

else:
    print("O número precisa ser maior ou igual a 10.")