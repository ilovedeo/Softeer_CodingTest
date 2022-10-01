import sys
import heapq

heap = []
price = 0

M, N = map(int, sys.stdin.readline().split())

for i in range(N):
    w, p = map(int, sys.stdin.readline().split())
    heapq.heappush(heap, (-p, w))

for i in range(N):
    (neg, w) = heap[0]
    # Bag is not full.
    if w < M:
        price = price + (-neg) * w
        M = M - w

    # The bag is full.
    else:
        price = price + (M * (-neg))
        break

    heapq.heappop(heap)

print(price)
