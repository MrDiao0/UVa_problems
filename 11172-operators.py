#UVa: 11172 - Relational operator
from sys import stdin

def main():
	cases = int(stdin.readline())
	for _ in range(cases):
		a,b = map(int,stdin.readline().split())
		if a==b: print('=')
		elif a>b: print('>')
		elif a<b: print('<')

main()