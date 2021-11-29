# Level 2

def solution(s):
	l = sol = 0
	for c in s:
		if c == '>':
			l += 1
		elif c == '<':
			sol += l
	return sol
