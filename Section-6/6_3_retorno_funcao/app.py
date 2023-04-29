def saudacao(nome):
    return "Olá %s" % nome

sds = saudacao("Kauan")

print(sds)

print(sds + ". Tudo bem?")

def soma(a, b):
    return a + b

s = soma(5, 7)
d = soma(2, 3)

print(s)

print(d)

print(s + d)

print(s + 10)
print(d + 14)


def profissao(nome):
    
    p = ""

    if nome == "Kauan":
        p = "Programador"
    else:
        p = "Não identificado"

    return p 

prof1 = profissao("João")

print(prof1)

prof2 = profissao("Kauan")

print(prof2) 