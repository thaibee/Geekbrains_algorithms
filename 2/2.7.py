n = int(input())
m1 = sum(i for i in range(n + 1))
m2 = n * (n+1) // 2
print(m1, m2, m1 == m2)
