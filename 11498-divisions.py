#UVa: 11498 - Divisions of Nlogonia
from sys import stdin

def main():
	k = int(stdin.readline())
	while k:
		n,m = map(int,stdin.readline().split())
		for _  in range(k):
			x,y = map(int,stdin.readline().split())
			if x==n or y==m: print("divisa")
			elif x>n and y>m: print("NE")
			elif x>n and y<m: print("SE")
			elif x<n and y>m: print("NO")
			elif x<n and y<m: print("SO")
		k = int(stdin.readline())

main()