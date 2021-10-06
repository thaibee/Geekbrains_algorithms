a = list(map(int, input('Enter 3 lengths of segments, separated by commas:').split(',')))
a = sorted(a)
if a[2] > a[0] + a[1]:
    print('Impossible  to construct a Triangle')
elif a[2] == a[0] + a[1]:
    print("It's a line")
elif a[2] == a[1] and a[1] == a[0]:
    print("It's a Equilateral triangle")
elif a[0] == a[1] or a[1] == a[2]:
    print("It's a Isosceles triangle")
else:
    print("It's a Scalene triangle")
