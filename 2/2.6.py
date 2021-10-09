import random

n = random.randint(0, 100)
c = 1
while c <= 10:
    m = int(input('Give me a number please:'))
    if m == n:
        print(f'Your guessed it! You used {c} attempts')
        break
    c += 1
    if c == 11:
        print(f'You guessed wrong, my number is:{n}')
        break
    if m > n:
        print('Your digit is bigger')
    else:
        print('Your digit is smaller')

