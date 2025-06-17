def calculate(vars, values, exp):
    slovar = zip(vars, values)
    slovar = dict(slovar)
    resul = ''
    for i in exp:
        if i in slovar:
            resul += str(slovar[i])
        if i == "-" or i == "+":
            resul += i

    return eval(resul)


print(calculate('xyz', [1, 2, 3], 'x-y+z'))             # 1 - 2 + 3 = 2

print(calculate('dbcw', [3, 0, -2, -3], '-d-c-b+w'))    # -3 - (-2) - 0 - 3 = -4

print(calculate('abcd', [0, 0, 0, 0], 'a+b+c+d'))       # 0 + 0 + 0 + 0 = 0

print(calculate('a', [4], 'a'))                         # 4 = 4

print(calculate('v', [-2], 'v'))                        # -2 = -2

print(calculate('ab', [2, 2], 'a+b'))                   # 2 + 2 = 4