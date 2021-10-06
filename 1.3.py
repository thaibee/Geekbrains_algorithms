import random
print(ord('z'), chr(122))
while True:
    m = input('Choise mode please\na - Integer\nb - Float\nc - Symbol\n q for exit\n?').lower()
    if m == 'a':
        a = list(map(int, input('Enter 2 Integer digits, separated by comma:').split(',')))
        print(random.randint(a[0], a[1]))
    elif m == 'b':
        a = list(map(float, input('Enter 2 Float digits, separated by comma:').split(',')))
        print(f'{random.uniform(a[0], a[1]):.4f}')
    elif m == 'c':
        a = input('Enter 2 symbols please, separated by comma:').split(',')
        print(chr(random.randint(ord(a[0]), ord(a[1]))))
    elif m == 'q':
        break
    else:
        print("Not correct symbol!")
# a = list(map(int, input('Enter coordinates point A, separated by commas:').split(',')))
