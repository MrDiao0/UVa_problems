#UVa: 11727 - Cost cutting
from sys import stdin

def main():
	aux = "Case {}: {}"
	cases = int(stdin.readline())
	for i in range(cases):
		X,Y,Z = map(int,stdin.readline().split())
		if Y<X<Z or Z<X<Y: print(aux.format(i+1,X))
		elif X<Y<Z or Z<Y<X: print(aux.format(i+1,Y))
		elif X<Z<Y or Y<Z<X: print(aux.format(i+1,Z))

main()