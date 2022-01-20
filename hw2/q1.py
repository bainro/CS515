
'''
Returns length of longest subsequence that's 
both increasing and alternating even/odd.
'''
def fast_LIS(a):
    n = len(a)
    if n == 0: 
        return 0

    # add sentinel to the end
    a.append(float('-inf'))
    
    # create n x n+1 array of 0s
    memo = [[0]*(n+1)]*n

    # iterate in reverse dir
    for j in range(n-1, -1, -1):
        # print("j: ", j)
        for i in range(-1, j):
            # print("i: ", i)
            keep = 1 + memo[j][j+1]
            skip = memo[i][j+1]
            # print(a[i], a[j])
            # print("type: ", type(a[i]))
            if a[i] > a[j] or same_parity(a[i], a[j]):
                # print("skip")
                memo[i][j] = skip
            else:
                # print("keep: ", keep)
                # print("skip: ", skip, "\n")
                memo[i][j] = max(keep, skip)

    print("memo: ", memo)
    return memo[0][0]

def same_parity(a, b):
    # special case for the sentinel value of neg infinity
    if a == float("-inf") or b == float("-inf"):
        return False
    return is_even(a) == is_even(b)

def is_even(v):
    return True if v % 2 == 0 else False

tests = []
answers = []

tests.append([])
answers.append(0)

tests.append([0])
answers.append(1)

tests.append([0, 2])
answers.append(1)

tests.append([0, 2, 0])
answers.append(1)

tests.append([0, 2, 1])
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
    print("test_a: ", test_a)
    print("result: ", result, "\n")
    assert answers[i] == result, f"WRONG! Correct answer was: {answers[i]}"
print("CORRECT! :)")