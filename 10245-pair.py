#UVa: 10245 - The Closest Pair Problem
from sys import stdin
from math import sqrt

inf = float('inf')

def solve(lo, hi):
	global pairs
	if lo+1 == hi:
		return inf
	mid = lo+((hi-lo)>>1)

	left = solve(lo,mid)
	right = solve(mid,hi)

	minim = inf
	dist = min(left,right)

	i = mid-1
	x,y = pairs[mid]
	x1,y1 = pairs[i]
	while i >= lo and abs(x-x1)<=dist:
		x1,y1 = pairs[i]
		x2,y2 = pairs[mid]
		j = mid
		while j < hi and abs(x1-x2)<=dist:
			x2,y2 = pairs[j]
			minim = min(minim, sqrt(pow(x1-x2,2)+pow(y1-y2,2)) )
			j += 1
		i -= 1

	return min(dist,minim)
	
def main():
	global pairs
	n = int(stdin.readline())
	while n:
		pairs = list()
		for _ in range(n): pairs.append(tuple(map(float,stdin.readline().split())))
		pairs.sort(key = lambda x:x[0])

		ans = solve(0,n)
		if ans<10000: print('{0:.4f}'.format(ans))
		else: print("INFINITY")

		n = int(stdin.readline())

main()