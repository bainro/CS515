# 2D list with each peg as a list
hanoi_board = None
last_p = 0
num_moves = 0

# used for ensuring legal moves
def check_board():
    global hanoi_board
    for i in range(len(hanoi_board)):
        p = hanoi_board[i]
        tmp = p.copy()
        tmp.sort()
        tmp.reverse()
        # should be the same as sorted & then reversed
        if tmp != p:
            return False
    return True

# move block from peg p -> q sequentially
def move(p, q):
    global num_moves
    global hanoi_board

    for i in range(abs(p-q)):
        num_moves += 1

        # moving block to the right
        if p < q:
            b = hanoi_board[p+i].pop()
            hanoi_board[p+i+1].append(b)
        else:
            b = hanoi_board[p-i].pop()
            hanoi_board[p-i-1].append(b)

        print(f"After move {num_moves}: ", hanoi_board)
        assert check_board(), "ILLEGAL MOVE YA MONKEY!"

def hanoi_liberty(n, p=0, a=None, mode=1):
    # n: number of blocks
    # p: peg number
    # a: number of adj moves to make
    global last_p, hanoi_board
       
    # can this be removed?
    if a == None:
        a = n-1

    # can be simplified
    if a <= 0 or p < 0:
        mode += 1
    
    if mode == 1:
        # print("unravel mode")
        move(p, p+a)
        return hanoi_liberty(n, p, a-1)
    elif mode == 2:
        print("reverse mode")
        for i in range(n, 1, -1):
            # shuffle decaying group to the right
            for j in range(1, i+1):
                s = last_p - j
                move(s, s+1)
            # last peg's block to the first unoccupide on the left
            move(last_p, last_p-i)
        return hanoi_liberty(n, n-2, 0, mode)
    elif mode == 3:
        print("restack mode")
        for i in range(-1, n-1):
            move(p-i, n)


hanoi_board = [[3,2,1],[],[],[]]
last_p = len(hanoi_board) - 1
n = len(hanoi_board[0])
print("n: ", n)
hanoi_liberty(n)
print("number of moves: ", num_moves)
