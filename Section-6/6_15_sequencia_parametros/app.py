def soma_todos(*nums):
    soma = 0
    for num in nums:
        soma += num

    return soma

s = soma_todos(1,1,2,2,3,3)

print(s)