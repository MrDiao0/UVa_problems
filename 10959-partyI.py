#UVa: 10959 - The Party, Part I
from collections import deque
from sys import stdin

def bfs(G,vis):
	queue = deque()
	queue.append((0,1))
	vis[0] = 0
	while len(queue):
		u,cnt = queue.popleft()
		for v in G[u]:
			if vis[v] == -1:
				queue.append((v,cnt+1))
				vis[v] = cnt

def main():
	cases = int(stdin.readline())
	for c in range(cases):
		empty = stdin.readline()
		n,m = map(int,stdin.readline().split())
		G = [[] for _ in range(n)]

		for _ in range(m):
			u,v = map(int,stdin.readline().split())
			G[u].append(v)
			G[v].append(u)

		vis = [-1 for _ in range(n)] 
		bfs(G,vis)

		for i in range(1,n):
			j = vis[i]
			print(j if j>-1 else 0)

		if c+1<cases: print()

main()