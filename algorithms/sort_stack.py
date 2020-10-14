# Cracking the Coding Interview Q3.5

def sort_stack(s1):
    s2 = []
    while s1:
        temp = s1.pop()
        while len(s2) != 0 and s2[-1] > temp:
            s1.append(s2.pop())
        s2.append(temp)
    while s2:
        s1.append(s2.pop())

