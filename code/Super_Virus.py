import sys

def product(p, n):
    # Termination condition.
    if n == 0:
        return pow(p, n)

    elif n % 2 == 0:
        temp = product(p, n // 2)
        return (temp * temp) % div

    else:
        temp = product(p, n // 2)
        return (temp * temp * p) % div

# N: init, P: proportion, N: time.
K, P, N = map(int, sys.stdin.readline().split())

time = int(N / 0.1)

div = 1000000007

Ans = K * product(P, time) % div

print(Ans)