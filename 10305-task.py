from sys import stdin

def solve():
	global graph,lenv
	n = len(graph)
	indeg = [0 for _ in range(n)]

	for lu in graph:
		for v in lu:
			indeg[v] += 1

	pending = [x for x in range(n) if indeg[x] == 0]

	ans = list()
	while len(pending)!=0:
		u = pending.pop()
		ans.append(u)
		for v in graph[u]:
			indeg[v] -= 1
			if indeg[v]==0: pending.append(v)

	return ans

def main():
	global graph,lenv
	lenv,lenb = map(int,stdin.readline().split())
	while lenv+lenb!=0:
		graph = [[] for _ in range(lenv)]
		
		for _ in range(lenb):
			n,m = map(int,stdin.readline().split())
			graph[n-1].append(m-1)

		ans = solve()
		for x in range(len(ans)):
			if x<len(ans)-1: print(ans[x]+1,end=' ')
			else: print(ans[x]+1,end='')
		print()
		lenv,lenb = map(int,stdin.readline().split())

main()