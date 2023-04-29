import random
x = random.randint(0, 10)

print("Adivinhe o número.")
chute = int(input("Chute um número de 0 a 10: "))

if chute == x:
    print("Você acertou o número correspondete a lista aleatória (%d)." %x)
else:
    print("Você errou o número correspondente a lista aleatória (%d)." %x)