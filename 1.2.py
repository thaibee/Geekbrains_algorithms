a = list(map(int, input('Enter coordinates for point A, separated by commas:').split(',')))
b = list(map(int, input('Enter coordinates for point B, separated by commas:').split(',')))

print(a, b)

if b[0] - a[0] == 0 and b[1] - a[1] == 0:
    print("It's point")
elif b[0] - a[0] == 0:
    print(f'x = {a[0]}')
elif b[1] - a[1] == 0:
    print(f'y = {a[1]}')
else:
    print(f'y = {-(a[0] * b[1] - b[0] * a[1])}/{b[0]-a[0]} + {-(a[1]-b[1])}/{b[0]-a[0]} * x')
