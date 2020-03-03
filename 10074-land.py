#UVa: 10074 - Take the Land
from sys import stdin

def search(L):
	n = len(L)
	queue = list()
	top,i,ans = 0,0,-1
	while i<n:
		if not len(queue) or L[i] >= L[queue[-1]]:
			queue.append(i)
			i += 1
		else:
			top = queue.pop()
			ans = max(ans,L[top]*((i-queue[-1]-1) if len(queue) else i))

	while len(queue):
		top = queue.pop()
		ans = max(ans,L[top]*((i-queue[-1]-1) if len(queue) else i))
	return ans

def solve(G,n,c):
	i,ans = 0,-1
	L = list()
	while i < n:
		e = G[i][c]
		if e>0:
			L.append(e)
		elif len(L):
			ans = max(ans,search(L))
			L = list()
		i += 1
	if len(L): ans = max(ans,search(L))
	return ans

def main():
	n,m = map(int,stdin.readline().split())
	while n+m:
		G = [[0 for _ in range(m)] for _ in range(n)]

		for i in range(n):
			j,cnt = 0,1
			for u in stdin.readline().split():
				if not int(u):
					G[i][j] = cnt
					cnt += 1
				else: cnt = 1
				j += 1

		ans = 0
		for r in range(m):
			ans = max(ans,solve(G,n,r))
		print(ans)

		n,m = map(int,stdin.readline().split())

main()