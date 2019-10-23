from sys import stdin

def mod(a,n,m):
	if n>1 and n%2==0:
		x = mod(a,n>>1,m)
		return (x*x)%m
	elif n>1:
		x = mod(a,(n-1)>>1,m)
		return (((x*x)%m)*a)%m
	else: return a

def main():
	aux = stdin.readline().strip()
	while len(aux):
		B = int(aux)
		p = int(stdin.readline())
		M = int(stdin.readline())

		print(mod(B,p,M) if p>0 else 1%M)

		empty = stdin.readline()
		aux = stdin.readline().strip()
main()