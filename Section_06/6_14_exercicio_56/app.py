def nome_(nome):
    print("Nome: %s." %nome)
    return nome

def idade_(idade):
    print("Idade: %d." %idade)
    return idade

def profissao_(profissao):
    print("Profissão: %s." %profissao)
    return profissao

a = nome_("Kauan")
b = idade_(18)
c = profissao_("Programador")

print(a,b,c)

print("Resolução de outra forma:")

def reune_dados(nome2, idade2, profissao2, fnct):
    apresentacao = fnct(nome2, idade2, profissao2)
    return apresentacao

def apresenta_dados(nome2, idade2, profissao2):
    frase = "O nome do usuário é %s e a sua idade é %d e ele é um %s." %(nome2, idade2, profissao2)
    return frase

print(reune_dados("Kauan", 18, "Programador", apresenta_dados))

apresentacao = reune_dados("Pedro", 40, "Engenheiro", apresenta_dados)

print(apresentacao)