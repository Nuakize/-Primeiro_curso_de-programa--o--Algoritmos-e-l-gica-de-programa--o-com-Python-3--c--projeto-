def media_notas(notas):
    media = 0
    soma = 0

    for n in notas:
        soma += n
    
    media = soma / len(notas)
    
    return media


notas = [9,8,7]

media_provas = media_notas(notas)

print(media_provas)
