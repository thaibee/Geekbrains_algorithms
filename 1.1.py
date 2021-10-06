a = 5
print(f'{a} = {bin(a)}')
b = 6
print(f'{b} = {bin(b)}')

# AND
print(f'{a} and {b} = {a & b} ({bin(a & b)})')

# OR
print(f'{a} or {b} = {a | b} ({bin(a | b)})')

# XOR
print(f'{a} xor {b} = {a ^ b} ({bin(a ^ b)})')

# Побитовый сдвиг вправо и влево(умножение и деление на 4)
print(f'{a << 2} = {bin(a << 2)}')
print(f'{a >> 2} = {bin(a >> 2)}')
