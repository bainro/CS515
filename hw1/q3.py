import statistics as s
import random as r
import math

'''
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

    print("a: ", a)
    m_a = median(a)
    print("m_a: ", m_a)
    print("b: ", b)
    m_b = median(b)
    print("m_b: ", m_b)

    if m_a == m_b:
        return m_a

    if len(a) == 2:
        max_ = max(a[0], b[0])
        min_ = min(a[1], b[1])
        return (max_ + min_) / 2
    else:
        # remove the largest & smallest elements
        i = math.ceil(len(a) / 2) # - 1
        print("i: ", i)
        if m_a > m_b:
            # A[:i], B[i:]
            return fastMedian(a[:i], b[i:])
            # A[i:], B[:i]
        return fastMedian(a[i:], b[:i])
'''

def getMedian(arr1, arr2, n):
     
    # there is no element in any array
    if n == 0:
        return -1
         
    # 1 element in each => median of
    # sorted arr made of two arrays will   
    elif n == 1:
        # be sum of both elements by 2
        return (arr1[0]+arr2[0])/2
         
    # Eg. [1,4] , [6,10] => [1, 4, 6, 10]
    # median = (6+4)/2   
    elif n == 2:
        # which implies median = (max(arr1[0],
        # arr2[0])+min(arr1[1],arr2[1]))/2
        return (max(arr1[0], arr2[0]) +
                min(arr1[1], arr2[1])) / 2
     
    else:
        #calculating medians    
        m1 = median(arr1, n)
        m2 = median(arr2, n)
         
        # then the elements at median
        # position must be between the
        # greater median and the first
        # element of respective array and
        # between the other median and
        # the last element in its respective array.
        if m1 > m2:
             
            if n % 2 == 0:
                return getMedian(arr1[:int(n / 2) + 1],
                        arr2[int(n / 2) - 1:], int(n / 2) + 1)
            else:
                return getMedian(arr1[:int(n / 2) + 1],
                        arr2[int(n / 2):], int(n / 2) + 1)
         
        else:
            if n % 2 == 0:
                return getMedian(arr1[int(n / 2 - 1):],
                        arr2[:int(n / 2 + 1)], int(n / 2) + 1)
            else:
                return getMedian(arr1[int(n / 2):],
                        arr2[0:int(n / 2) + 1], int(n / 2) + 1)
 
 # function to find median of array
def median(arr, n):
    if n % 2 == 0:
        return (arr[int(n / 2)] +
                arr[int(n / 2) - 1]) / 2
    else:
        return arr[int(n/2)]

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
    m = getMedian(a, b, len(a))
    print("a: ", a)
    print("b: ", b)
    print("predicted: ", m)
    print("real answer: ", real_m, "\n")
    assert m == real_m, "WRONG!"
print("CORRECT!")
