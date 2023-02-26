import math


def solve(A):
    n = A[0]
    gcd = 0
    for i in range(1, len(A)):
        gcd = math.gcd(n, A[i])
    return gcd <= 2

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(a))

# print(solve([1261,227821,143,4171,1941]))
