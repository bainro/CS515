import statistics as s
import random as r

def median(c):
    m_i = len(c) // 2
    # if list has even number of ele's
    if len(c) % 2 == 0:
        avg = (c[m_i-1] + c[m_i]) / 2
        return avg
    return c[m_i]

def fastMedian(a, b, n):
    # there is no element in any array
    if n == 0:
        return None
    elif n == 1:
        return (a[0] + b[0]) / 2
    elif n == 2:
        max_ = max(a[0], b[0])
        min_ = min(a[1], b[1])
        return (max_ + min_) / 2
    else:
        m_a = median(a)
        m_b = median(b)

        i = int(n / 2)
        # include a's median value
        if m_a > m_b:
            if n % 2 == 0:
                # the smaller if median is an avg
                return fastMedian(a[:i+1], b[i-1:], i+1)
            else:
                # the median value exists in the list
                return fastMedian(a[:i+1], b[i:], i+1)
        # include b's median value
        else:
            if n % 2 == 0:
                # the smaller if median is an avg
                return fastMedian(a[i-1:], b[:i+1], i+1)
            else:
                # the median value exists in the list
                return fastMedian(a[i:], b[:i+1], i+1)

# random test cases with n from [0, 6]
a_s = []
b_s = []
for _ in range(10):
    for i in range(0, 7):
        a = [r.randrange(-15, 15, 1) for _ in range(i)]
        a.sort()
        a_s.append(a)
        b = [r.randrange(-15, 15, 1) for _ in range(i)]
        b.sort()
        b_s.append(b)

for a, b in zip(a_s, b_s):
    # s.median errors on empty list
    try:
        real_m = s.median(a + b)
    except:
        real_m = None
    m = fastMedian(a, b, len(a))
    print("a: ", a)
    print("b: ", b)
    print("predicted: ", m)
    print("real answer: ", real_m, "\n")
    assert m == real_m, "WRONG!"
print("CORRECT!")
