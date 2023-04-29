lista = [0,1,2,3,4,5,6,7,8,9]

i = 0

while i < 10:
    lista.append(i)
    i=i+1

print(lista)

j = 0

while j < len(lista):
    if lista[j] == 4:
        del lista[j]
    j=j+1

print(lista)