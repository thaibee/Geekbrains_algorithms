a = input("Enter 2 symbols, separated by comma please\n").split(',')
print(f'{a[0]} - symbol #{ord(a[0])-96}')
print(f'{a[1]} - symbol #{ord(a[1])-96}')
print(f'between them {abs(ord(a[1]) - ord(a[0]) - 1)} symbols')
