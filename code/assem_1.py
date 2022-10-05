import sys
import random

K, N = map(int, sys.stdin.readline().split())

# 2 x 2 vector for assembly.
dyn = [[0 for i in range(K)] for j in range(N)]

for lvl in range(N):
    assem = list(map(int, sys.stdin.readline().split()))
    # assem = random.sample(list(range(1, 101)), (K + K * (K - 1)))

    grid = []

    # Initial condition.
    if lvl == 0:
        dyn[0] = assem[0: K]
        mov_prev = assem[K:]

    # Make grid delay vector.
    else:
        for j in range(K):
            start = (K - 1) * j
            grid = grid + [mov_prev[start: start + j] + [0] + mov_prev[start + j: start + (K - 1)]]

        for j in range(K):
            mov_delay = [grid[i][j] for i in range(K)]
            prev_delay = list(map(sum, zip(mov_delay, dyn[lvl - 1])))
            dyn[lvl][j] = assem[j] + min(prev_delay)

        mov_prev = assem[K:]

print(min(dyn[N - 1]))