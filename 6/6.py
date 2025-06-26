def check_letters(s):
    s = s.lower()
    finish = []
    for i in range(26):
        target = chr(ord('a') + i)
        if target in s:
            finish.append(1)
        else:
            finish.append(0)
    l = "".join([str(i) for i in finish])
    return l

print(check_letters('ABcd'))
print(check_letters('A-Z'))
print(check_letters('b*e*e*g*e*e*k'))
print(check_letters('a'))
print(check_letters('Привет!'))
print(check_letters('abcdefghijklmnopqrstuvwxyz'))