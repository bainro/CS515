import statistics as s
import random as r
import math

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

    if len(a) == 0:
        print("a==[]; b: ", b)
        return median(b)
    elif len(b) == 0:
        print("b==[]; a: ", a)
        return median(a)

    print("a: ", a)
    m_a = median(a)
    print("m_a: ", m_a)
    print("b: ", b)
    m_b = median(b)
    print("m_b: ", m_b)

    if m_a == m_b:
        return m_a
    if len(a) == 1:
        return (a[0] + b[0]) / 2
    if len(a) == 2:
        max_ = max(a[0], b[0])
        min_ = min(a[1], b[1])
        return (max_ + min_) / 2
    else:
        # remove the largest & smallest elements
        i = math.ceil(len(a) / 2)
        print("i: ", i)
        if m_a > m_b:
            return fastMedian(a[:i], b[i:])
        return fastMedian(a[:i], b[i:])


# random test cases with n from [1, 6]
a_s = []
b_s = []
for i in range(1, 7):
    a = [r.randrange(-15, 15, 1) for _ in range(i)]
    a.sort()
    a_s.append(a)
    b = [r.randrange(-15, 15, 1) for _ in range(i)]
    b.sort()
    b_s.append(b)

for a, b in zip(a_s, b_s):
    real_m = s.median(a + b)
    m = fastMedian(a, b)
    print("a: ", a)
    print("b: ", b)
    print("predicted: ", m)
    print("real answer: ", real_m, "\n")
    assert m == real_m, "WRONG!"
print("CORRECT!")
