frase = "Eu quero encontrar o peixe!"
print(frase.find("peixe"))

if frase.find("peixe") >= 0:
    print("Encontrei o peixe.")

print(frase.find("sapato"))

if frase.find("sapato") >= -1:
    print("Não há sapato na frase.")
else:
    print("Há sapato na frase")