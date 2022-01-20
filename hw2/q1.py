
'''
Returns length of longest subsequence that's 
both increasing and alternating wrt parity.
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
            if a[i] > a[j]:
                # print("skip")
                memo[i][j] = skip
            else:
                # print("keep: ", keep)
                # print("skip: ", skip, "\n")
                memo[i][j] = max(keep, skip)

    print("memo: ", memo)
    return memo[0][0]

test_a = [4, 0, 2, 0, 1]
result = fast_LIS(test_a)
print("test_a", test_a)
print("result: ", result)