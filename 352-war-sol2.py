from sys import stdin

drow = [-1,-1,-1,0,0,1,1,1]
dcol = [-1,0,1,-1,1,-1,0,1]

def dfs(row,col):
	global vis,n
	queue = [(row,col)]
	vis[row][col] = 0
	while len(queue):
		r,c = queue.pop()
		for u in range(8):
			dr,dc = r+drow[u],c+dcol[u]
			if 0<=dr<n and 0<=dc<n and vis[dr][dc]==1:
				queue.append((dr,dc))
				vis[dr][dc] = 0

def solve():
	global vis,n
	cnt = 0
	for r in range(n):
		for c in range(n):
			if vis[r][c] == 1:
				cnt += 1
				dfs(r,c)
	return cnt

def main():
	global vis,n
	cnt,msg = 1,"Image number {} contains {} war eagles."
	line = stdin.readline().strip()
	while len(line):
		vis = list()
		n = int(line)
		for _ in range(n):
			vis.append([int(u) for u in stdin.readline().strip()])

		print(msg.format(cnt,solve()))
		line = stdin.readline().strip()
		cnt += 1

main()