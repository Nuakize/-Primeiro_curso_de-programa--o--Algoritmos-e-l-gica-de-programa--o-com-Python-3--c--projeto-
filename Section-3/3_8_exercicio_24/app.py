n1 = int(input("Insira um número para ser multiplaco: "))
n2 = int(input("Insira outro número para multiplcar com o primeiro: "))

multiplicacao = n1 * n2
if  multiplicacao >= 100:
    print("Número alto %d." %multiplicacao)
else:
    print("Número baixo %d." %multiplicacao)
