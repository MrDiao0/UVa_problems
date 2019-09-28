#UVa 10009 - All roads lead where?
from collections import deque
from sys import stdin

def bfs(src,tgt):
	global G,cities
	n = len(G)
	visited = [-1 for _ in range(n)]
	queue = deque()
	visited[src] = 1
	queue.append((src,cities[src]))
	while len(queue) and visited[tgt]==-1:
		u,ans = queue.popleft()
		for v in G[u]:
			if visited[v] == -1:
				visited[v] = 1
				queue.append((v,ans+cities[v]))
	return ans+cities[tgt]

def main():
	global G,cities
	cases = int(stdin.readline())
	for case in range(cases):
		cities,repeated = dict(),set()
		empty = stdin.readline()
		m,n = map(int,stdin.readline().split())
		cnt = 0
		G = list()
		for _ in range(m):
			line = stdin.readline().split()
			a,b = line[0][0],line[1][0]
			if a not in repeated:
				repeated.add(a)
				cities[a] = cnt
				cities[cnt] = a
				cnt += 1

			if b not in repeated:
				repeated.add(b)
				cities[b] = cnt
				cities[cnt] = b
				cnt += 1

			while len(G)<cnt: G.append([])
			G[cities[a]].append(cities[b])
			G[cities[b]].append(cities[a])

		for _ in range(n):
			line = stdin.readline().split()
			src,tgt = line[0][0],line[1][0]
			print(bfs(cities[src],cities[tgt]))

		if case < cases-1: print()

main()