#UVa: 10669 - Three Powers
from sys import stdin

def solve(num):
	ans = list()
	for i in range(len(num)):
		if num[i]=='1': ans.append(pow(3,i))
	return ans

def main():
	line = int(stdin.readline())
	while line:
		n = bin(line-1)[2:]
		l = [i for i in n]
		l.reverse()
		ans = solve(l)

		print('{ ',end='')
		for u in range(len(ans)):
			if u!=len(ans)-1:
				print("{}, ".format(ans[u]),end='')
			else: print(ans[u],end=' ')
		print('}')
		line = int(stdin.readline())

main()