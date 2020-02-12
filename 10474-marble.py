#UVa: 10474 - Where is the Marble? 
from sys import stdin

inf = float('inf')

def main():
	cases = 1
	n,q = map(int,stdin.readline().split())
	while n+q:
		
		l = list()
		m = -inf
		for _ in range(n):
			i = int(stdin.readline())
			l.append(i)
			m = max(m,i)

		isit = [False for _ in range(m+1)]
		aux = [0 for _ in range(m+1)]
		for u in l: aux[u] += 1; isit[u] = True

		acum = aux[:]
		for u in range(1,m+1): acum[u] += acum[u-1]

		
		print("CASE# {}:".format(cases))
		for _ in range(q):
			i = int(stdin.readline())
			if i<=m and isit[i]:
				print("{} found at {}".format(i,acum[i]-aux[i]+1))
			else:
				print("{} not found".format(i))
		
		n,q = map(int,stdin.readline().split())
		cases += 1

main()