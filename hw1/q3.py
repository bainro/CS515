import statistics as s
import math as m

def median(c):
    # floor division
    m_i = len(c) // 2
    # if list has even number of ele's
    if len(c) % 2 == 0:
        avg = (c[m_i-1] + c[m_i]) / 2
        return avg
    return c[m_i]

def fastMedian(a, b):
    # print("fx called!")
    m_a = median(a)
    m_b = median(b)
    if m_a == m_b:
        return m_a
    if len(a) == 1:
        return (a[0] + b[0]) / 2
    else:
        # remove the largest & smallest elements
        r = m.ceil(len(a) / 2)
        if m_a > m_b:
            # remove largest in a & smallest in b
            return fastMedian(a[:-1 * r], b[r:])
        # remove largest in b & smallest in a
        return fastMedian(a[r:], b[:-1 * r])

a = [0, 1, 5, 8, 9]
b = [0, 3, 6, 6, 9]
real_m = s.median(a + b)
m = fastMedian(a, b)
print("a: ", a)
print("b: ", b)
print("predicted: ", m)
print("real answer: ", real_m)
assert m == real_m, "WRONG!"
print("CORRECT!")
