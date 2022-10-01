import sys
import bisect

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

# Forward board.
fwd_board = []
forward = [1] * N

# Inverse board
inv_board = []
inverse = [0] * N

for i, fwd in enumerate(data):
    # Find forward index.
    # 1. Initial condition. No revision on the forward tabel.
    if len(fwd_board) == 0:
        fwd_board.append(fwd)

    # 2. If fwd is the biggest: append fwd at the end.
    elif fwd > fwd_board[-1]:
        fwd_board.append(fwd)
        forward[i] = len(fwd_board)

    # 3. If there is bigger element in the board: change infimum element as fwd.
    else:
        idx = bisect.bisect_left(fwd_board, fwd)
        fwd_board[idx] = fwd
        forward[i] = forward[i] + idx


    # Find inverse index.
    inv = data[N - (i + 1)]
    # 1. Initial condition. No revision on the inverse tabel.
    if len(inv_board) == 0:
        inv_board.append(inv)

    # 2. If inv is the biggest: append fwd at the end.
    elif inv > inv_board[-1]:
        inv_board.append(inv)
        inverse[N - (i + 1)] = len(inv_board) - 1

    # 4. If there is bigger element in the board: change infimum element as fwd.
    else:
        idx = bisect.bisect_left(inv_board, inv)
        inv_board[idx] = inv
        inverse[N - (i + 1)] = inverse[N - (i + 1)] + idx

total = list(map(sum, zip(forward, inverse)))

print(max(total))
