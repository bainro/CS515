# 2D list with each peg as a list
hanoi_board = None
num_moves = 0

# used for ensuring legal moves
def check_board():
    global hanoi_board
    for _ in range(len(hanoi_board)):
        p = hanoi_board[i]
        tmp = p.copy()
        tmp.sort()
        tmp.reverse()
        # should be the same as sorted & then reversed
        if tmp != p
            return False
    return True

# move block from peg p -> q sequentially
def move(p, q):
    global num_moves
    global hanoi_board

    # moving block to the left vs right
    if p < q:
        r_iter = range(1, p-q+1, 1)
    else:
        r_iter = range(-1, p-q-1, -1)    
        
    for i in range(r_iter):
        num_moves += 1
        # move last # from list[p] to list[p-1]
        b = hanoi_board[p].pop()
        hanoi_board[p+i].append(b)
        assert check_board(), "ILLEGAL MOVE YA MONKEY!"

def hanoi_extra_peg(n, p=0, q=n-1, mode=1):
    # n: number of blocks
    # p: peg number
    # q: number of adj moves

    if q == 0:
        mode += 1
    
    # mode 1: unravel
    if mode == 1:
        move(p, p+q)
        return hanoi_extra_peg(n, p, q-1)
    # mode 2: reverse order
    elif mode == 2:
        move(p, p+q)
        return hanoi_extra_peg(n, p, q-1)
    # mode 3: restack
    elif mode == 3:
        move(p, p+q)
        return hanoi_extra_peg(n, p-1, q+1)
    else:
        return num_moves

hanoi_board = [[3,2,1],[],[],[]]
hanoi_extra_peg()





'''
def move(src, dest, tmps, top_call=False):
    if len(tmps) > 0:
        move(src, tmps[0], tmps[1:])
        move_top_block(src, dest) # moves top block of src to dest
        if top_call:
            for p in tmps:
                move_top_block(p, dest) # move each tmp peg block to END

def move_top_block(s, d):
    pass
'''
