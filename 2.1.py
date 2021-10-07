
while True:
    a, b = map(int, input('Enter two digits separated by comma, please:\n?').replace(' ', '').split(','))
    c = input('Enter method please:\n+ for adding\n- for deduction\n* for multiplication\n/ for division\n0 for exit\n?')
    if c == '+':
        result = a + b
    elif c == '-':
        result = a - b
    elif c == '*':
        result = a * b
    elif c == '/':
        result = a // b
    elif c == '0':
        result = a + b
        break
    else:
        print('Incorrect data')
        continue
    print(f'{a}{c}{b}={result}')



