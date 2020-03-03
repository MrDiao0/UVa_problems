#UVa: 11658 - Best Coalitions
from math import floor
from sys import stdin

def round_half_up(n, dec):
	mult = 10 ** dec
	return floor(n*mult + 0.5) / mult

def solve(l,n,e):
	mem,aux = set(),set()
	mem.add(e)
	ans = 10001
	for u in l:
		aux = mem.copy()
		for v in aux:
			tmp = u+v
			if tmp not in aux:
				mem.add(tmp)
				if 5000 < tmp < ans: ans = tmp

	return round_half_up((100*e)/ans,2)

def main():
	n,m = map(int,stdin.readline().split())
	while n+m:
		l = list()
		for _ in range(n):
			l.append(float(stdin.readline())*100)
		e = l[m-1]
		l[m-1] = l[-1]
		l.pop()

		if e<5000: print("{0:.2f}".format(solve(l,n-1,e)))
		else: print('100.00')

		n,m = map(int,stdin.readline().split())

main()