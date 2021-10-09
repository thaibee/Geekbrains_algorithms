for i in range(32, 128):
    n = ' ' if i < 100 else ''
    print(f'{i}={chr(i)}{n}', end=' ')
    if i % 10 == 1:
        print()
