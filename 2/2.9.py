n = int(input())
m = [input() for i in range(n)]
m_item = m_sum = 0
for i in m:
    t = sum(map(int, i))
    if t > m_sum:
        m_sum = t
        m_item = i
print(m_item, m_sum)
