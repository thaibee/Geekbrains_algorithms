while True:
    a, b = map(int, input('Enter two digits separated by comma, please:\n?').replace(' ', '').split(','))
    c = input(
        'Enter method please:\n+ for adding\n- for deduction\n* for multiplication\n/ for division\n0 for exit\n?')
    if c == '0':
        break
    elif c == '+':
        result = a + b
    elif c == '-':
        result = a - b
    elif c == '*':
        result = a * b
    elif c == '/':
        if b == 0:
            print('division by 0')
            continue
        result = a // b
    else:
        print('Incorrect data')
        continue
    print(f'{a}{c}{b}={result}')
