from sys import stdin
from collections import deque

pos = [[-1,0],[0,-1],[1,0],[0,1]]

def bfs(src):
	global visited
	ans = 0
	queue = deque()
	if visited[src[0]][src[1]]!=1: queue.append(src)
	while len(queue):
		u,v = queue.popleft()
		for i in pos:
			deltax = v+i[0]
			deltay = u+i[1]
			if visited[deltay][deltax] == 0:
				visited[deltay][deltax] = 2
				queue.append(( deltay, deltax))
			elif visited[deltay][deltax] == 3:
				visited[deltay][deltax] = 2
				queue.append(( deltay, deltax))
				ans += 1
			elif visited[deltay][deltax] == 4:
				visited[deltay][deltax] = 1
				ans += 1

		visited[u][v] = 2
	return ans

def main():
	#0: Vacio,1: Posicion peligrosa,2:Muro/visitado ,3 Oro,4 Oro con posicion peligrosa
	global visited
	line = stdin.readline().split()
	while len(line):
		x,y = map(int,line)
		visited = [[0 for _ in range(x)] for _ in range(y)]

		for i in range(y):
			line = stdin.readline().strip()
			for j in range(x):
				if line[j]=='P':
					src = [i,j]
				if line[j]=='#':
					visited[i][j] = 2
				if line[j]=='G':
					if visited[i][j]==1:
						visited[i][j] = 4
					else:
						visited[i][j] = 3
				if line[j]=='T':
					visited[i][j] = 2
					for t in pos:
						deltax = j+t[0]
						deltay = i+t[1]
						if visited[deltay][deltax]==3:
							visited[deltay][deltax] = 4
						elif visited[deltay][deltax] == 0:
							visited[deltay][deltax] = 1
		print(bfs(src))
		line = stdin.readline().split()

main()