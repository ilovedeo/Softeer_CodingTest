import sys

count = 0

# Define recursion function.
def find_bigger(Max, list_recur):
    # First condition: termination
    if len(list_recur) == 0:
        return 0

    # If there is bigger number on the left, then return fragment of the list.
    # And add 1 to count.
    else:
        global count
        count = count + 1
        # print(count)

        # Filter the bigger element.
        filtered = list(filter(lambda n: n > Max, list_recur))

        # Escape procedure.
        if len(filtered) == 0:
            return 0

        # Recursive procedure.
        # print(filtered)
        find_bigger(filtered[0], filtered)

#########################################################
# Get input.
#########################################################

# The number of the rock.
N = int(sys.stdin.readline())

# Get data.
data = list(map(int, sys.stdin.readline().split()))

find_bigger(data[0], data)

print(count)