from sys import stdin

def maximun(l):
	n = l.index(max(l))
	aux = l[n]
	tmp = l[-1]
	l[-1] = l[n]
	l[n] = tmp
	l.pop()
	return [max(l),aux]

def solve(G,n):
	global l,visited
	visited[n] = 1
	k = 0
	tmp = list()

	for u in range(len(G[n])):
		if visited[G[n][u][0]] == 0:
			c = G[n][u][1] + solve(G,G[n][u][0])
			tmp.append(c)

	if len(tmp) > 1:
		m = maximun(tmp)
		k = m[0] + m[1]
		l[n] = k
		return m[1]


	elif len(tmp) == 1:
		l[n] = tmp[0]
		return tmp[0]
	else:
		return k

def main():
	global l,visited

	line = stdin.readline().split()
	while len(line):
		G = [[]for _ in range(10000)]
		l = [0 for _ in range(10000)]
		visited = [0 for _ in range(10000)]
		while len(line):
			line = list(map(int,line))

			G[line[0]-1].append((line[1]-1,line[2]))
			G[line[1]-1].append((line[0]-1,line[2]))

			line = stdin.readline().split()
		i = 0
		while len(G[i])==0:i+=1
		solve(G,i)
		print(max(l))
		line = stdin.readline().split()
main()