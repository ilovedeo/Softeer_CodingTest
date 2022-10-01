import sys

# The number of the rock.
N = int(sys.stdin.readline())

# Get data.
data = list(map(int, sys.stdin.readline().split()))

check = [1] * N

for i, Max in enumerate(data):
    # Spit out bigger element's index.
    idx_list = list(filter(lambda idx: data[idx] < Max, range(i + 1)))
    # Case 1: len(filtered) is zero.
    if len(idx_list) == 0:
        pass

    # Case 2: len(filtered) is not zero.
    else:
        # Identify the biggest element of the check[idx_list].
        check[i] = max([check[j] for j in idx_list]) + 1
print(check)
print(max(check))