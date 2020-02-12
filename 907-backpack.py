#UVa: 907 - Winterim Backpacking Trip
from sys import stdin

def isin(N,K,lim):
	global camps
	n,k,dist = 0,0,0
	while k<=K and n!=N:
		if dist+camps[n]<=lim: dist+=camps[n]; n+=1
		else: k+=1; dist=0
	return k<=K

def main():
	global camps
	line = stdin.readline().split()
	while len(line):
		n,k = map(int,line)
		n += 1

		camps = list()
		for _ in range(n): camps.append(int(stdin.readline()))

		lo,hi = 0,sum(camps)
		while lo+1!=hi:
			mid = lo+((hi-lo)>>1)
			if isin(n,k,mid): hi=mid
			else: lo=mid

		print(hi)

		line = stdin.readline().split()
	
main()