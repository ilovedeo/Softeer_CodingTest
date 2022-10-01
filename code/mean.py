import sys

# Shape of the data.
N, K = map(int, sys.stdin.readline().split())

# Get data and index : line 0 stores the data.
total_data = [list(map(int, sys.stdin.readline().split())) for i in range(K + 1)]

data = total_data[0]

for idx in total_data[1:]:
    idx_data = data[idx[0] - 1: idx[1]]
    mean = sum(idx_data) / len(idx_data)
    print("{:.2f}".format(mean))