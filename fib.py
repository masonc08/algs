def fib(n):
    if n < 0:
        raise Exception()
    if n == 0 or n == 1:
        return 1
    sol = [0, 1]
    i = 2
    while i <= n:
        next_fib = sol[0] + sol[1]
        sol[0] = sol[1]
        sol[1] = next_fib
        i += 1
    return sol[1]

