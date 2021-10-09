n = int(input('Enter quantity:'))
s = input('Enter the desired symbol:')
m = sum((input(f'Enter line #{i+1}:').count(s)) for i in range(n))
print(f'quantity: {m}')
