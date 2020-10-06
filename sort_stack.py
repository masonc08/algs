# Cracking the Coding Interview Q3.5

def sort_stack(s1):
    s2 = []
    while s1:
        temp = s1.pop()
        xfered = 0
        while len(s2) != 0 and s2[-1] < temp:
            s1.append(s2.pop())
            xfered += 1
        s2.append(temp)
        while xfered != 0:
            s2.append(s1.pop())
            xfered -= 1
    while s2:
        s1.append(s2.pop())

