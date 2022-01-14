def in_order(a, k, k_i=-1):
    # 1st call is when last_i needs to be called 2x
    if k_i == -1:
        k_i = last_i(a, k)
        if k_i == -1:
            return False

    if k == 1:
        return True
    else:
        left_a = a[:k_i-1]
        j_i = last_i(a, k-1)
        if j_i != -1 and in_order(left_a, k-1, j_i):
            return True
        else:
            return False

'''
# Fang's very similar version. Let's call it version B
def in_order(a, k):
    if k == 1:
        return True
    else:
        k_i = last_i(a, k)
        left_a = a[:k_i]
        ### main difference:
        ### going & finding it in list but not saving the index/location!
        if k-1 in left_a and in_order(left_a, k-1):
            print("k: ", k)
            return True
        else:
            return False
'''

# find the index of the last occurrence of k
def last_i(a, k):
    k_i = -1
    for i in range(len(a)-1, -1, -1):
            if a[i] == k:
                k_i = i
    return k_i

test_1 = []
test_2 = [1, 2, 4, 5, 3, 4]
test_3 = [1, 2, -4, 5, 3, 4]
test_4 = [1, 2, 2, 4, 4, 6, 7]
test_5 = [2]
test_6 = [1]
test_7 = [1, 2, 3, 4, 5, 6] # example worst case!

assert in_order(test_1, 0) == False, "WRONG!"
# version B doesn't pass, wrong base case
assert in_order(test_1, 1) == False, "WRONG!"
assert in_order(test_2, 3) == True,  "WRONG!"
assert in_order(test_2, 4) == False, "WRONG!"
assert in_order(test_3, 4) == True,  "WRONG!"
assert in_order(test_4, 1) == True,  "WRONG!"
# version B doesn't pass, doesn't check first k exists
assert in_order(test_4, 3) == False, "WRONG!"
assert in_order(test_4, 4) == False, "WRONG!"
assert in_order(test_5, 1) == False, "WRONG!"
assert in_order(test_6, 1) == True,  "WRONG!"
assert in_order(test_6, 2) == False, "WRONG!"
assert in_order(test_7, 6) == True,  "WRONG!"

print("CORRECT!")
