
'''
Returns length of longest subsequence that's 
both increasing and alternating even/odd.
'''
def fast_LIS(a):
    n = len(a)
    if n == 0 or n == 1: 
        return n

    # add sentinel to the end
    a.append(float('-inf'))
    
    # create n x n+1 array of 0s
    memo = [[0]*(n+1)]*n

    # iterate in reverse dir
    for j in range(n-1, -1, -1):
        # print("j: ", j)
        for i in range(-1, j):
            # print("i: ", i)

            even = is_even(a[j])
            skip = memo[i][j+1]        
            keep = memo[j][j+1]

            if keep == 0:
                if even:
                    keep = -1
                else:
                    keep = 1
            elif keep > 0:
                keep += 1
            else:
                keep -= 1

            # fucked up for base case?
            alternating = True    
            if keep > 0 and even:
                alternating = False
            elif keep < 0 and not even:
                alternating = False
            
            print("alternating: ", alternating)
            print("a[i]: ", a[i], "a[j]: ", a[j])
            # test! won't work long term because 0 could be anywhere in a[]
            # if a[j] == 0:
            #     alternating = True

            is_larger = a[i] <= a[j] # if a[i] != float("-inf") else False
            keep_larger = abs(keep) > abs(skip)
            larger_and_alt = (is_larger and alternating and keep_larger)
            if larger_and_alt:
                print("kept!")
                memo[i][j] = -1 * keep
            else:
                memo[i][j] = skip

            print("keep: ", keep)
            print("skip: ", skip, "\n")
                

    print("memo: ", memo)
    return abs(memo[0][0])

def same_parity(a, b):
    # special case for the sentinel value of neg infinity
    if a == float("-inf") or b == float("-inf"):
        return False
    return is_even(a) == is_even(b)

def is_even(v):
    return True if v % 2 == 0 else False

tests = []
answers = []

# tests.append([])
# answers.append(0)

tests.append([0])
answers.append(1)

# tests.append([0, 2])
# answers.append(1)

tests.append([0, 1])
answers.append(2)

tests.append([0, 2])
answers.append(1)

# tests.append([0, 2, 0])
# answers.append(1)

tests.append([0, 2, 1])
answers.append(2)

tests.append([1, 3, 2])
answers.append(2)

tests.append([0, 2, 1, 1, 3])
answers.append(2)

tests.append([0, 2, 1, 1, 3, 2])
answers.append(3)

tests.append([0, 2, 1, 1, 3, 2, 2])
answers.append(3)

tests.append([4, 0, 2, 0, 1, 2, 2, 4, 9])
answers.append(4)

for i, test_a in enumerate(tests):
    result = fast_LIS(test_a)
    print("test_a: ", test_a) # ignore -inf
    print("result: ", result, "\n")
    assert answers[i] == result, f"WRONG! Correct answer was: {answers[i]}"
print("CORRECT! :)")
