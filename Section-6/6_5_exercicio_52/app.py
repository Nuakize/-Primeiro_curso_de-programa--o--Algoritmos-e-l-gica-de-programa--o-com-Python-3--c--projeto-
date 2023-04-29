def contador_caracteres(texto):
    contador = ""

    if len(texto) >= 20:
        contador = "Texto longo."
    else:
        contador = "Texto curto."
    return contador

textao = contador_caracteres("SAPATO ENSAPATADOS SAPATIADOS SAPATOS.")
textin = contador_caracteres("SAPATO.")

print(textao)
print(textin)