from sys import stdin

def dfs(u):
	
	for v in G[u]:
		if depth[v]==-1:
			son[u] += 1
			depth[v] = low[v] = depth[u]+1
			parents[v] = u
			dfs(v)
			low[u] = min(low[u], low[v])

			if parents[u] == -1 and son[u]>1 or depth[u] <= low[v] and parents[u] != -1:
				ans.add(u)

		else: low[u] = min(low[u], depth[v])

	return ans


def tarjan():
    global depth, low, parents, son, ans
    ans = set()
    n = len(G)

    depth = [-1 for _ in range(n)]
    low = [-1 for _ in range(n)]
    parents = [-1 for _ in range(n)]
    son = [0 for _ in range(n)]

    for i in range(n):
        if depth[i]==-1:
        	depth[i] = low[i] = 0
        	dfs(i)

    return len(ans)

def main():
	global G
	case = int(stdin.readline().strip())
	while case!=0:
		G = [[] for _ in range(case)]
		line = [int(i) for i in stdin.readline().split()]
		
		while(line[0]!=0):
		
			for i in range(len(line)-1):
				G[line[0]-1].append(line[i+1]-1)
				G[line[i+1]-1].append(line[0]-1)
			line = [int(i) for i in stdin.readline().split()]
		
		print(tarjan())
		
		case = int(stdin.readline().strip())

main()