import sys

N = int(sys.stdin.readline())
assem = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

dyn = [[0, 0]] * N
dyn[0] = [assem[0][0], assem[0][1]]

for i in range(1, N):
    # dyn[i] = [A_i, B_i]
    dyn[i] = [min(dyn[i - 1][0], dyn[i - 1][1] + assem[i - 1][3]) + assem[i][0],
              min(dyn[i - 1][1], dyn[i - 1][0] + assem[i - 1][2]) + assem[i][1]]

print(min(dyn[N - 1]))