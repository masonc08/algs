def solve(A, s):
    m, n = len(A), len(A[0])
    for row in A:
        if s in row or s in reversed(row): # O(N(K+M))
            return True
    for col in zip(*A):
        if s in col or s in reversed(col): # O(M(K+N))
            return True
    for i in range(n):
        k = 0
        cur, cur2 = [], []
        while 0 <= i+k < n or 0 <= k < m:
            cur.append(A[i+k][k])
            cur2.append(A[i+k][-k-1])
        curstring, curstring2 = "".join(cur), "".join(cur2)
        if s in curstring or s in reversed(curstring) or s in curstring2 or s in reversed(curstring2): # O(N(K+max(M,N)))
            return True
    for j in range(1, m):
        k = 0
        cur, cur2 = [], []
        while 0 <= k < n or 0 <= j+k < m:
            cur.append(A[k][j+k])
            cur2.append(A[k][-j-1-k])
        curstring = "".join(cur)
        curstring, curstring2 = "".join(cur), "".join(cur2)
        if s in curstring or s in reversed(curstring) or s in curstring2 or s in reversed(curstring2): # O(N(K+max(M,N)))
            return True
    return False
