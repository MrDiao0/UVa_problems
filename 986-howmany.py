#UVa: 986 - How many?
from sys import stdin

def phi(x,y,r,d,mem): #True = UP, False = Down
	global n,k
	ans = 0
	if (x,y,r,d) in mem:
		ans = mem[(x,y,r,d)]
	else:
		if x==(n<<1):
			if (not y) and (not r):
				ans = 1
		else:
			if y==0:
				ans = phi(x+1,y+1,r,True,mem)
			else:
				if not d or (d and y!=k):
					ans = phi(x+1,y+1,r,True,mem) + phi(x+1,y-1,r,False,mem)
				if d and y == k:
					if r==0:
						ans = phi(x+1,y+1,r,True,mem)
					else:
						ans = phi(x+1,y+1,r,True,mem) + phi(x+1,y-1,r-1,False,mem)
		mem[(x,y,r,d)] = ans
	return ans

def main():
	global n,k
	line = stdin.readline().split()
	while len(line):
		n,r,k = map(int,line)

		print(phi(0,0,r,False,dict()))
		line = stdin.readline().split()

main()