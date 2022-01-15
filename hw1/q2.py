### GLOBALS
board = None
last_p = 0
num_moves = 0

# used for ensuring legal moves
def check_board():
    global board
    for i in range(len(board)):
        p = board[i]
        tmp = p.copy()
        tmp.sort()
        tmp.reverse()
        # should be the same as sorted & then reversed
        if tmp != p:
            return False
    return True

# move block from peg p -> q 1 peg at a time
def move(p, q):
    global num_moves
    global board

    for i in range(abs(p-q)):
        num_moves += 1

        # moving block to the right
        if p < q:
            b = board[p+i].pop()
            board[p+i+1].append(b)
        else:
            b = board[p-i].pop()
            board[p-i-1].append(b)

        print(f"After move {num_moves}: ", board)
        assert check_board(), "ILLEGAL MOVE!"

# n: number of blocks
# p: peg index
    # mode 1: move this peg's top block
    # mode 2: move block to this peg
# a: number of adj moves to make
# mode: 1.unravel, 2.reverse, 3.restack
def liberty_hanoi(n, p=0, a=0, mode=1):   
    global last_p, board

    if a <= 0:
        mode += 1
    
    if mode == 1:
        # print("mode 1: unravel")
        move(p, p+a)
        return hanoi_liberty(n, p, a-1)
    elif mode == 2:
        # print("mode 2: reverse")
        for i in range(n, 1, -1):
            # shuffle decaying group to the right
            for j in range(1, i+1):
                s = last_p - j
                move(s, s+1)
            # last peg's block to the first unoccupided on the left
            move(last_p, last_p-i)
        return hanoi_liberty(n, n-2, 0, mode)
    elif mode == 3:
        # print("mode 3: restack")
        for i in range(-1, n-1):
            move(p-i, n)

# test boards!
boards = []
boards.append([[]])
boards.append([[1],[]])
boards.append([[2,1],[],[]])
boards.append([[3,2,1],[],[],[]])
boards.append([[4,3,2,1],[],[],[],[]])
boards.append([[5,4,3,2,1],[],[],[],[],[]])
boards.append([[6,5,4,3,2,1],[],[],[],[],[],[]])
boards.reverse()

for board in boards:
    num_moves = 0
    last_p = len(board) - 1
    n = len(board[0])
    liberty_hanoi(n, a=n-1)
    print(f"number of moves for n={n}: ", num_moves, "\n")
    assert num_moves >= 3 * n^2 or not n, "bounds reported incorrectly!"
