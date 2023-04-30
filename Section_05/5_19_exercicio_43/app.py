l = [1,2,3,4,5]

n1 = int(input("Digite o primeiro número de 1 a 5: "))
n2 = int(input("Digite o segundo de 1 a 5: "))

achou = False

i = 0

while i < len(l):
    if l[i] == n1:
        print("O primeiro número (%d) está na frente do segundo número digitado na lista!" % n1)
    elif l[i] == n2:
        print("O segundo número (%d) está na frente do primeiro número digitado na lista!" % n2)
    break
    
i = i + 1
