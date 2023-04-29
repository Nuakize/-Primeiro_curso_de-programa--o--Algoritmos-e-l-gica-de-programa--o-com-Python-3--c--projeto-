lista1 = ["Sapato", "azul", 20.50]
lista2 = ["Camiseta", "amarela", 120.99]
lista3 = ["Calça jeans", "preta", 60.50]

lista_pai = [lista1, lista2, lista3]

print(lista_pai)

for produto in lista_pai:
    print("O produto %s da cor %s sairá por %.2f" %(lista1[0], lista2[1], lista3[2]))
    break