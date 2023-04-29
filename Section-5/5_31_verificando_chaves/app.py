dicionario = {
    "Testando": 2,
    "Nome": "Kauan",
    "Idade": 18,
}

print(dicionario)

print("Nome" in dicionario)
print("Sobrenome" in dicionario)

if "Nome" in dicionario:
    print("O seu nome é %s" % dicionario["Nome"])

print(dicionario["Sobrenome"])