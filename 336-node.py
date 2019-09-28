from collections import deque
from sys import stdin

def bfs(src,TTL):
	global G,vis,cnt
	queue = deque()
	queue.append((src,TTL))
	vis[src] = 1
	while len(queue):
		u,t = queue.popleft()
		cnt += 1
		for v in G[u]:
			if not vis[v] and t:
				queue.append((v,t-1))
				vis[v] = 1

def next_N():
	global i, INPUT
	while(INPUT[i].isdigit()==False and INPUT[i]!='-'):
		i+=1
	j=i+1
	while(j<len(INPUT) and INPUT[j].isdigit()):
		j+=1
	ans = int(INPUT[i:j])
	i=j
	return ans

def main():
	global i, INPUT, G, vis, cnt
	INPUT = stdin.read()
	i,case = 0,1
	ans = "Case {}: {} nodes not reachable from node {} with TTL = {}."

	n = next_N()
	while n > 0:
		G = []
		nodes,aux = dict(),0
		repeated = set()

		for _ in range(n):
			u,v = str(next_N()),str(next_N())
			if u not in repeated:
				G.append([])
				repeated.add(u)
				nodes[u] = aux
				nodes[aux] = u
				aux += 1

			if v not in repeated:
				G.append([])
				repeated.add(v)
				nodes[v] = aux
				nodes[aux] = v
				aux += 1
			
			G[nodes[u]].append(nodes[v])
			G[nodes[v]].append(nodes[u])

		node,TTL = next_N(),next_N()
		while node+TTL>0:
			if str(node) in repeated:
				u = nodes[str(node)]
				cnt = 0
				vis = [0 for _ in range(len(G))]
				bfs(u,TTL)
				print(ans.format(case,len(G)-cnt,nodes[u],TTL))
			else: print(ans.format(case,len(G),node,TTL))
			node,TTL = next_N(),next_N()
			case += 1

		n = next_N()

main()