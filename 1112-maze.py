#UVa: 1112 - Mice and Maze
from heapq import heappop,heappush
from sys import stdin

inf = float('inf')

def dijkstra():
	ans = inf
	visited = [False for _ in range(n)]
	dist = [inf for _ in range(n)]
	queue,dist[src] = [(0,src)],0

	while len(queue):
		d,u = heappop(queue)
		if visited[u]==False:
			visited[u] = True
			for v,w in G[u]:
				tmpd = d+w
				if visited[v]==False and dist[v]>tmpd:
					dist[v] = tmpd
					heappush(queue,(tmpd,v))

	return dist

def main():
	global G,n,src
	cases = int(stdin.readline())
	for i in range(cases):
		empty = stdin.readline()
		n = int(stdin.readline())
		G = [[] for _ in range(n)]
		src = int(stdin.readline())-1
		T = int(stdin.readline())
		M = int(stdin.readline())
		for _ in range(M):
			a,b,w = map(int,stdin.readline().split())
			if a!=b:
				G[b-1].append((a-1,w))

		mices = dijkstra()
		ans = 0
		for mice in mices:
			if mice<=T: ans += 1
		print(ans)
		#print(mices,T)
		if i<cases-1: print()

main()