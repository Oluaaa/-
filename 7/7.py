def get_oldest(args):
    max_age = 0
    name = []
    for k, v in args.items():
        if v > max_age:
            max_age = v
    for k, v in args.items():
        if v == max_age:
            name.append(k)
    return min(name)


print(get_oldest({'Тимур': 31, 'Валерий': 34, 'Артур': 24, 'Анастасия': 28, 'Антон': 21, 'Сослан': 27}))

print(get_oldest({'Лариса': 35, 'Антон': 21, 'Сослан': 27, 'Тимур': 31, 'Артур': 41}))

print(get_oldest({'Тимур': 31}))

print(get_oldest({'Лариса': 18, 'Анастасия': 18}))

print(get_oldest({'Пантелеймон': 34, 'Нина': 34, 'Любовь': 25, 'Станислав': 34}))

print(get_oldest({'Елисей': 49, 'Сидор': 31, 'Василиса': 21, 'Мирон': 40, 'Юрий': 26}))