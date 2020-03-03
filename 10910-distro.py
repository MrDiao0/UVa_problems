#UVa: 10910 - Marks Distribution
from sys import setrecursionlimit as SRL
from sys import stdin
SRL(10000)

def binom(n, k, memo):
	ans,key = None,(n, k)
	if key in memo: ans = memo[key]
	else:
		if k==0 or k==n: ans = 1
		else:
			if n<(k<<1): k = n-k
			ans = binom(n-1, k-1,  memo) + binom(n-1, k, memo)
		memo[key] = ans
	return ans

def main():
	mem = dict()
	cases = int(stdin.readline())
	for _ in range(cases):
		n,t,p = map(int,stdin.readline().split())
		lim = t-(n*p)
		if lim >= 0:
			print(binom(lim+n-1,n-1,mem))
		else:
			print(0)
			
main()