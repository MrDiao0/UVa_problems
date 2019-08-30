from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10000)

def dfs(u):
	
	for v in G[u]:
		if depth[v]==-1:
			son[u] += 1
			depth[v] = low[v] = depth[u]+1
			parents[v] = u
			dfs(v)
			if parents[u] == -1 and son[u]>1 or depth[u] <= low[v] and parents[u] != -1:
				con[u] += 1
			low[u] = min(low[u], low[v])

		else: low[u] = min(low[u], depth[v])

	return


def tarjan():
    global depth, low, parents, son, con
    n = len(G)

    con = [1 for _ in range(n)]
    depth = [-1 for _ in range(n)] 
    low = [-1 for _ in range(n)]
    parents = [-1 for _ in range(n)]
    son = [0 for _ in range(n)]

    for i in range(n):
        if depth[i]==-1:
        	depth[i] = low[i] = 0
        	dfs(i)

    return

def main():
	global G
	n,m = map(int,stdin.readline().split())
	while n and m:
		G = [[] for _ in range(n+1)]
		u,v = map(int,stdin.readline().split())
		while u!=-1 and v!=-1:
			G[u].append(v)
			G[v].append(u)
			u,v = map(int,stdin.readline().split())

		tarjan()

		for i in range(m):
			pigeon = max(con)
			print(con.index(pigeon),con[con.index(pigeon)])
			con[con.index(pigeon)] = -1
		print()

		n,m = map(int,stdin.readline().split())

main()