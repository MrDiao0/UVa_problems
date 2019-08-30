from sys import stdin

def solve(T):
	global ans
	if len(T)==1: ans += T
	elif len(T)>1: 
		solve(T[1])
		solve(T[2])
		solve(T[0])
	return

def parse(preo,ino):
	Tree = []
	if len(ino):
		i = 0
		Tree = [preo[0]]
		while i<n and ino[i]!=preo[0]: i += 1
		Tree.append(parse(preo[1:i+1],ino[0:i])) #Left
		Tree.append(parse(preo[i+1:],ino[i+1:])) #Right

	return Tree
	
def main():
	global n,ans
	cases = int(stdin.readline().strip())
	for _ in range(cases):
		ans = ""
		n,preord,inord = stdin.readline().split()
		n = int(n)
	
		T = parse(preord,inord)
		solve(T)
		print(ans)

main()