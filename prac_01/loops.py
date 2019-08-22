for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 110, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number_stars = int(input("How many stars would you like? "))

for i in range(number_stars):
    print('*', end='')
print()

for i in range(1, number_stars + 1):
    print('*' * i)
print()
