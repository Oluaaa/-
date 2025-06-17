def make_palindrome(n):
    if str(n) == str(n)[::-1]:
        return n
    n = int(str(n)[::-1])
    for i in range(5):
        n = int(str(n)[::-1]) + n
        if str(n) == str(n)[::-1]:
            return n
    return -1

print(make_palindrome(101))
print(make_palindrome(23))
print(make_palindrome(196))
print(make_palindrome(1))
print(make_palindrome(166))
print(make_palindrome(69))