#UVa: 10496 - Collecting Beepers
from sys import stdin
#from sys import setrecursionlimit as SRL
#SRL(10000)
inf = float('inf')

def solve(dist,pos,mask,mem,n,lim):
	ans = inf
	if mask == lim: ans = dist[pos][0]
	if (pos,mask) in mem: ans = mem[(pos,mask)]
	else:
		for i in range(n):
			if not mask&(1<<i):
				ans = min(ans,solve(dist,i,mask|(1<<i),mem,n,lim)+dist[pos][i])
		mem[(pos,mask)] = ans
	return ans

def main():
	global x0,y0
	cases = int(stdin.readline())
	for _ in range(cases):
		lenx,leny = map(int,stdin.readline().split())
		x0,y0 = map(int,stdin.readline().split())
		b = int(stdin.readline())
		
		l = list()
		l.append((x0,y0))
		for _ in range(b):
			l.append(tuple(map(int,stdin.readline().split())))

		b += 1
		dist = [[0 for _ in range(20)] for _ in range(20)]
		for u in range(b):
			for v in range(u+1,b):
				x1,y1 = l[u]
				x2,y2 = l[v]
				auxd = abs(x1-x2)+abs(y1-y2)
				dist[u][v],dist[v][u] = auxd,auxd

		print("The shortest path has length {}".format(solve(dist,0,0,dict(),b,(1<<b)-1)))

main()