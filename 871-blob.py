from sys import stdin

deltar = [-1,-1,-1,0,0,1,1,1]
deltac = [-1,0,1,-1,1,-1,0,1]

def main():
	cases = int(stdin.readline())
	empty = stdin.readline()
	for cas in range(cases):
		i = 0
		vis = list()
		aux = stdin.readline().strip()
		lenc = len(aux)
		while len(aux):
			vis.append([])
			for e in aux: vis[i].append(int(e))
			aux = stdin.readline().strip()
			i += 1

		lenr = len(vis)
		ans = 0
		queue = []

		for r in range(lenr):
			for c in range(lenc):
				if vis[r][c] == 1:
					cnt = 0
					queue.append((r,c))
					vis[r][c] = 0
					while len(queue):
						cnt += 1
						dr,dc = queue.pop()
						for j in range(8):
							delr,delc = dr+deltar[j],dc+deltac[j]
							if 0<=delr<lenr and 0<=delc<lenc and vis[delr][delc]==1:
								queue.append((delr,delc))
								vis[delr][delc] = 0
					if cnt > ans: ans = cnt
		print(ans)
		if cas<cases-1: print()

main()