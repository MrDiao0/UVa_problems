from sys import stdin

def dfs(u,num):
	global vis, scc, G
	vis[u] = 1
	scc[u] = num
	for v in G[u]:
		if(vis[v] == 0):
			dfs(v,num)
	return

def dfs_list(u):
	global L, vis, I
	vis[u] = 1
	for v in I[u]:
		if(vis[v] == 0):
			dfs_list(v)
	L.append(u)
	return


def Kosajaru(G):
	global L,I, scc, vis
	n = len(G)
	scc = [-1 for i in range(n)]

	I = [[] for i in range(n)]
	for i in range(n):
		for j in G[i]:
			I[j].append(i)
	vis = [0 for i in range(n)]
	L = []
	for i in range(n):
		if(vis[i] == 0):
			dfs_list(i)
	vis = [0 for i in range(n)]
	cont = 0
	while(len(L)):
		i = L.pop()
		if(vis[i] == 0):
			dfs(i,cont)
			cont +=	1
	return cont

def main():
	global G
	line = stdin.readline().split()
	while len(line)>0 and line[0]!='0':
		
		c,r = map(int,line) #Cases / Relations
		P,arcs = {},[] #Personal
		for i in range(c):
			#aux = stdin.readline().split()
			P[stdin.readline().strip()] = i

		G = [[] for _ in range(len(P))]

		for _ in range(r):
			aux = stdin.readline().strip()
			aux1 = stdin.readline().strip()
			G[P.get(aux)].append(P.get(aux1))
		print(G)
		print(Kosajaru(G))

		line = stdin.readline().split()

main()