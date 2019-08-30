#UVa: 10986 - Sending email
from sys import stdin
from heapq import heappush,heappop
	
inf = float('inf')

def solve():
	ans = inf
	visited = [False for _ in range(n)]
	parents = [None for _ in range(n)]
	dist = [inf for _ in range(n)]
	queue,dist[src] = [(0,src)],0

	while visited[tgt]==False and len(queue):
		d,u = heappop(queue)
		if visited[u]==False:
			visited[u] = True
			for v,w in G[u]:
				tmpd = d+w #Dist u->v
				if visited[v]==False and dist[v]>tmpd:
					dist[v],parent[v] = tmpd,u
					heappush(queue,(tmpd,v))

	return dist[tgt]

def main():
	global G,n,src,tgt
	cases = int(stdin.readline())

	for i in range(cases):
		n,m,src,tgt = map(int,stdin.readline().split())
		G = [[] for _ in range(n)]

		for _ in range(m):
			u,v,w = map(int,stdin.readline().split())
			if u!=v:
				G[u].append((v,w))
				G[v].append((u,w))

		ans = solve()
		if ans==inf: ans = "unreachable"

		aux = "Case #{}: {}"
		print(aux.format(i+1,ans))

main()