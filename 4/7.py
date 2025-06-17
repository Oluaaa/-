def snake(n):
    side = 'right'
    for i in range(n):
        if i % 2 == 0:
            print('*' * n)
        elif side == 'left':
            print('*')
            side = 'right'
        elif side == 'right':
            print(' ' * (n - 1) + '*')
            side = 'left'

snake(1)
print()
snake(3)
print()
snake(4)
print()
snake(5)
print()
snake(10)
print()
snake(50)