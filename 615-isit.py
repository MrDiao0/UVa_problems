from sys import stdin
from collections import deque

def bfs(G,u,visited):
	queue = deque()
	queue.append(u)
	visited[u] = 1
	while len(queue):
		u = queue.popleft()
		for v in G[u]:
			if visited[v]==0:
				visited[v] = 1
				queue.append(v) 
	return


def check(outdeg,indeg):
	ans = True
	cnt = 0
	for i in range(len(indeg)): 
		if indeg[i] == 0: cnt += 1; parent = i
		if indeg[i] > 1 : ans = False
	if cnt != 1: ans = False

	if ans==True:
		visited = [0 for _ in range(len(outdeg))]
		bfs(outdeg,parent,visited)
		for i in visited:
			if i==0: ans = False
	if len(outdeg)==0: ans = True
	return ans

def solve(a):
	
	major,aux = {},set()
	cnt = 0

	for i in a:
		if not i[0] in aux: major[i[0]] = cnt; cnt += 1
		aux.add(i[0])
		if not i[1] in aux: major[i[1]] = cnt; cnt += 1
		aux.add(i[1])

	G = [[] for _ in range(len(aux))]
	indeg = [0 for _ in range(len(aux))]

	for i in range(len(a)):
		indeg[major.get(a[i][1])] += 1
		G[major.get(a[i][0])].append(major.get(a[i][1]))
	
	return check(G,indeg)

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
	global i, INPUT
	INPUT=stdin.read()

	i=0
	cnt=1
	case1="Case {} is a tree."
	case2="Case {} is not a tree."
	a,b = next_N(),next_N()
	
	while( a >= 0 or b>=0):
		Trees=[]
		
		while(a>0 or b>0):
			Trees.append((a,b))
			a,b = next_N(),next_N()
		
		a,b = next_N(),next_N()
		ans = solve(Trees)
		
		if(ans):
			print(case1.format(cnt))
			cnt+=1
		
		else:
			print(case2.format(cnt))
			cnt+=1

main()