#UVa: 929 - Number Maze
from sys import stdin
from heapq import heappop,heappush

deltar = [-1,0,0,1]
deltac = [0,-1,1,0]

inf = float('inf')

def dijkstra(G,src,tgt):
	global row,col
	s0,s1,t0,t1 = src[0],src[1],tgt[0],tgt[1]
	ans = inf
	visited = [[False for _ in range(col)] for _ in range(row)]
	dist = [[inf for _ in range(col)] for _ in range(row)]
	queue,dist[s0][s1] = [(G[s0][s1],s0,s1)],G[s0][s1]

	while visited[t0][t1]==False and len(queue):
		d,r,c = heappop(queue)
		if visited[r][c]==False:
			visited[r][c] = True
			for i in range(4):
				dr,dc = r+deltar[i],c+deltac[i]
				if 0<=dr<row and 0<=dc<col:
					tmpw = d+G[dr][dc]
					if visited[dr][dc]==False and dist[dr][dc]>tmpw:
						dist[dr][dc] = tmpw
						heappush(queue,(tmpw,dr,dc))
	return dist[t0][t1]

def main():
	global row,col
	cases = int(stdin.readline())
	for _ in range(cases):
		row = int(stdin.readline())
		col = int(stdin.readline())
		maze = list()

		for _ in range(row): maze.append(list(map(int,stdin.readline().split())))

		ans = dijkstra(maze,(0,0),(row-1,col-1))
		print(ans)

main()