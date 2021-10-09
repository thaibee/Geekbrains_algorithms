n = int(input())
result = 0
item = 1
while n > 0:
    result += item
    n += -1
    item /= -2
print(result)
