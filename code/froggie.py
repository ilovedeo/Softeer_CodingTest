import sys

N, M = map(int, sys.stdin.readline().split())
w_list = list(map(int, sys.stdin.readline().split()))

best = [1] * N

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())

    if w_list[A - 1] > w_list[B - 1]:
        best[B - 1] = 0

    elif w_list[A - 1] < w_list[B - 1]:
        best[A - 1] = 0

    else:
        best[A - 1] = 0
        best[B - 1] = 0

print(sum(best))
