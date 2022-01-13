import statistics as s

def median(c):
    print("[median(c)] c: ", c)
    # floor division
    m_i = len(c) // 2
    print("[median(c)] m_i: ", m_i)
    # if list has even number of ele's
    if len(c) % 2 == 0:
        avg = (c[m_i-1] + c[m_i]) / 2
        return avg
    return c[m_i]

def fastMedian(a, b):
    m_a = median(a)
    m_b = median(b)
    if m_a == m_b:
        return m_a
    if len(a) == 2:
        if m_a > m_b:
            avg = (a[0] + b[1]) / 2
            return avg
        avg = (a[1] + b[0]) / 2
        return avg
    else:
        # remove the largest & smallest elements
        if m_a > m_b:
            # remove largest in a & smallest in b
            return fastMedian(a[:-1], b[1:])
        # remove largest in b & smallest in a
        return fastMedian(a[1:], b[:-1])

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
