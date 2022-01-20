
'''
Returns length of longest subsequence that's 
both increasing and alternating wrt parity.
'''
def fast_LIS(a):
    n = len(a)

    # add sentinel to the end
    a.append(float('-inf'))
    
    # create 2d array of 0s
    memo = [[0]*n]*n

    # iterate in reverse dir
    for j in range(n-1, -1, -1):
        # normal forward dir
        for i in range(j-1):
            keep = 1 + memo[j, j+1]
            skip = memo[i, j+1]
            if a[i] >= a[j]:
                