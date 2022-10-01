import sys
import heapq

N = int(sys.stdin.readline())

heap = []

for i in range(N):
    s, f = map(int, sys.stdin.readline().split())
    heapq.heappush(heap, (f, s))

# Initial condition for endtime.
endtime = 0
count = 0

while heap:
    f, s = heapq.heappop(heap)

    # If new start time is larger than previous endtime:
    if s >= endtime:
        count = count + 1
        endtime = f

print(count)