# 2D list with each peg as a list
hanoi_board = None
num_moves = 0

def check_pegs():
    global hanoi_board
    for _ in range(len(hanoi_board)):
        p = hanoi_board[i]
        tmp = p.copy()
        tmp.sort()
        tmp.reverse()
        if tmp != p
            return False
    return True

def move(p, q):
    # p: start peg number
    # n: end peg number

    global num_moves
    global hanoi_board

    # moving peg to the left
    if p > q:
        for i in range(abs(p-q)):
            num_moves += 1
            # move last # from list[p] to list[p-1]
            b = hanoi_board[p].pop()
            hanoi_board[p-i].append(b)
            # assert that each peg (represented as an array) is decraseing order
    else:
        pass
    
    assert check_pegs(), "ILLEGAL MOVE YA MONKEY!"

def hanoi_extra_peg(n, p, q=n-1, mode=1):
    # n: number of blocks
    # p: peg number
    # q: number of adj moves

    # mode 1: unravel
    if mode == 1:
        move(p, p+q)
        hanoi_extra_peg(n, p, q-1)
    # mode 2: reverse order
    elif mode == 2:
        pass
    # mode 3: restack
    elif mode == 3:
        move(p, )
        hanoi_extra_peg(n, p, q-1)

    if mode < 3:
        hanoi_extra_peg(n, p, None, mode=mode+1)
    else:
        return num_moves

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
