escopo_global = "Tchau."
numero = 15

def escopo_local():
    numero = 10
    escopo_local = "Olá."
    print(escopo_local)
    print(escopo_global)

    if numero == 10:
        print("Você ganhou.")

escopo_local()

escopo_global = "Até logo."

escopo_local()