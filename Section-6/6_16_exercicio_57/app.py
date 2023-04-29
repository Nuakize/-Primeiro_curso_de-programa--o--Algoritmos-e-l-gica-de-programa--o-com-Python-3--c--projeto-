def mult_todos(*nums):
    multiplicacao = 1
    for num in nums:
        multiplicacao *= num

    return multiplicacao


m = mult_todos(10, 10)

print(m)