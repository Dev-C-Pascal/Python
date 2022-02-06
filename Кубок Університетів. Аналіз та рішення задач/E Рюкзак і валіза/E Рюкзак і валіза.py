s = int(input())
m_r, m_v = 0, 0
n = int(input())

for i in range(n):
    m = int(input())
    if m_r + m < s:
        m_r += m
    else:
        m_v += m
print(m_r)
print(m_v)
