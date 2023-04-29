notas = [5.5, 8.0, 4.5, 6.0, 5.0]

print(notas)

i = 0

soma = 0

while i < 4:
    soma = soma + notas[i]
    i = i + 1

media = soma / 5

if media >= 5.0:
    print("O aluno passou de ano.  %.1f" %media)
else:
    print("O aluno reprovou.  %.1f" %media)