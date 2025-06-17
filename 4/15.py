def longest_substring_without_vowels(s):
    glas = ['a', 'e', 'i', 'o', 'u']
    finish = []
    stroka = ''
    for i in s:
        if i not in glas:
            stroka += i
        else:
            finish.append(stroka)
            stroka = ''
        finish.append(stroka)
    return len(max(finish))


print(longest_substring_without_vowels('abcdefg'))
print(longest_substring_without_vowels('bcdgf'))
print(longest_substring_without_vowels('aeiou'))
print(longest_substring_without_vowels('abecidofug'))
print(longest_substring_without_vowels('x'))
print(longest_substring_without_vowels('abbbabbaba')) 