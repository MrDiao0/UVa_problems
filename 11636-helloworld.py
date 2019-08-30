#UVa: 11636 - Hello world
from math import ceil,log2
from sys import stdin

def main():
	cnt,aux = 1,"Case {}: {}"
	n = int(stdin.readline())
	while n>0:
		if n: print(aux.format(cnt,ceil(log2(n))))
		else: print(aux.format(cnt,0))
		n = int(stdin.readline())
		cnt += 1

main()