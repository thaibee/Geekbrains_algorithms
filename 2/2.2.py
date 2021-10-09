n = '34560'
result = [0] * 2
for i in n:
    if int(i) % 2 == 0:
        result[0] += 1
    else:
        result[1] += 1
print(f'even:{result[0]}\nodd:{result[1]}')
