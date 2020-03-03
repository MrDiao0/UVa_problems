#UVa: 572 - Oil Deposits
from sys import stdin

deltar = [-1,0,1,-1,1,-1,0,1]
deltac = [-1,-1,-1,0,0,1,1,1]

def dfs(G,r0,c0):
	global lenr,lenc
	queue = list()
	queue.append((r0,c0))
	G[r0][c0] = 1
	while len(queue):
		r,c = queue.pop()
		for i in range(8):
			dr = r + deltar[i]
			dc = c + deltac[i]
			if 0<=dr<lenr and 0<=dc<lenc and not G[dr][dc]:
				G[dr][dc] = 1
				queue.append((dr,dc))

def main():
	global lenr,lenc
	lenr,lenc = map(int,stdin.readline().split())
	while lenr+lenc:
		G = [[-1 for _ in range(lenc)] for _ in range(lenr)]
		
		for r in range(lenr):
			line = stdin.readline().strip()
			for c in range(lenc):
				if line[c] == '@': G[r][c] = 0

		ans = 0
		for r in range(lenr):
			for c in range(lenc):
				if not G[r][c]:
					ans += 1
					dfs(G,r,c)

		print(ans)

		lenr,lenc = map(int,stdin.readline().split())

main()
