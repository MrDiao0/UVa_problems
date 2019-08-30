from sys import stdin

def solve(T,acum):
	global ans
	if len(T)==1:
		if T[0]==1:
			ans += acum
	elif len(T):
		aux = acum >> 2
		solve(T[1],aux)
		solve(T[2],aux)
		solve(T[3],aux)
		solve(T[4],aux)
	return

def sum(T1,T2):
	if T1[0] == 1 or T2[0] == 1:
		Tree = [1]
	else:
		if len(T1)==1: Tree = T2
		elif len(T2)==1: Tree = T1
		else:
			Tree = [0]
			Tree.append(sum(T1[1],T2[1]))
			Tree.append(sum(T1[2],T2[2]))
			Tree.append(sum(T1[3],T2[3]))
			Tree.append(sum(T1[4],T2[4]))

	return Tree

def parse(T):
	global i
	Tree = []
	if i<len(T)-1:
		i += 1
		if T[i]=='p':
			Tree = [0]
			Tree.append(parse(T))
			Tree.append(parse(T))
			Tree.append(parse(T))
			Tree.append(parse(T))
		elif T[i]=='e':
			Tree = [0]
		elif T[i]=='f':
			Tree = [1]
	return Tree

def main():
	global i,ans
	cases = int(stdin.readline().strip())
	for _ in range(cases):
		ans = 0
		left = stdin.readline().strip()
		right = stdin.readline().strip()

		i = -1
		T1 = parse(left)
		i = -1
		T2 = parse(right)

		solve(sum(T1,T2),1024)

		print("There are {} black pixels.".format(ans))


main()