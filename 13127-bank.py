#UVa 13127 - Bank Robery
from heapq import heappop,heappush
from sys import stdin

inf = float('inf')

def solve():
	ans = inf
	visited = [False for _ in range(n)]
	dist = [inf for _ in range(n)]
	queue = []
	for u in police:
		heappush(queue,(0,u))
		dist[u] = 0
	
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
	global n,G,src,police
	line = stdin.readline().split()
	while len(line):
		n,M,B,P = map(int,line)
		G = [[] for _ in range(n)]

		for _ in range(M):
			a,b,w = map(int,stdin.readline().split())
			if a!=b:
				G[a].append((b,w))
				G[b].append((a,w))

		banks = []
		police = []
		if B>0: banks = [int(v) for v in stdin.readline().split()]
		if P>0: police = [int(u) for u in stdin.readline().split()]

		dists = solve()
		ans = []
		for i in banks:
			ans.append((dists[i],i))

		maxbanks = []
		aux = maxdist = max(ans)
		while aux[0] == maxdist[0]:
			pos = ans.index(aux)
			maxbanks.append(ans[pos][1])
			ans[pos] = (-1,-1)
			aux = max(ans)

		if maxdist[0] == inf: maxdist = ('*',inf)
		maxbanks.sort()
		
		print(len(maxbanks),maxdist[0])
		for v in range(len(maxbanks)):
			if v<len(maxbanks)-1: print(maxbanks[v],end=' ')
			else: print(maxbanks[v])

		line = stdin.readline().split()


main()