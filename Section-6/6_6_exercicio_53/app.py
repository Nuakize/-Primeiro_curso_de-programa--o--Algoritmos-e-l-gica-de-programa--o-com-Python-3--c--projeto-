def retorna_lista_par(l):
    nova_lista = []

    for numero in l:
        if numero % 2 == 0:
            nova_lista.append(numero)

    return nova_lista

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

lista_par = retorna_lista_par(lista)

print(lista_par)