
'''
Returns length of longest subsequence that's 
both increasing and alternating wrt parity.
'''
def fast_LIS(a):
    n = len(a)

    # add sentinel to the end
    a.append(float('-inf'))
    
    # create 2d array of 0s
    memo = [[0]*(n+1)]*n

    # iterate in reverse dir
    for j in range(n-1, -1, -1):
        # normal forward dir
        for i in range(-1, j-1):
            keep = 1 + memo[j][j+1]
            skip = memo[i][j+1]
            # print(a[i], a[j])
            if a[i] >= a[j]:
                # print("skip")
                memo[i][j] = skip
            else:
                print("keep: ", keep)
                print("skip: ", skip, "\n")
                memo[i][j] = max(keep, skip)

    print("memo: ", memo)
    return memo[0][1]

test_a = [0, 1, 2]
result = fast_LIS(test_a)
print("test_a", test_a)
print("result: ", result)