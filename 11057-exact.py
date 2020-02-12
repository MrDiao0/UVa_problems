#UVa: 11057 - Exact Sum
from sys import stdin

def binSearch(n,n1):
	global nums
	lo,hi = 0,len(nums)-1
	while hi-lo > 1:
		mid = lo+((hi-lo)>>1)
		if n > nums[mid]: lo = mid
		elif n < nums[mid]: hi = mid
		elif n==nums[mid]: lo = hi = mid
	if nums[lo]==n and lo!=n1: return (True,n)
	if lo-1>=0 and nums[lo-1]==n and lo-1!=n1: return (True,n)
	if lo+1<len(nums) and nums[lo+1]==n and lo+1!=n1: return (True,n)

	return (False,0)

def main():
	global nums
	line = stdin.readline().strip()
	while len(line):
		n = int(line)
		nums = list(map(int,stdin.readline().split()))
		nums.sort()

		m = int(stdin.readline())
		a,b = 1000002,0
		for i in range(n):
			f = binSearch(abs(m-nums[i]),i)
			if f[0] and (abs(a-b)>abs(nums[i]-f[1])): a,b = min(nums[i],f[1]),max(nums[i],f[1])

		print("Peter should buy books whose prices are {} and {}.\n".format(a,b))

		empty = stdin.readline()
		line = stdin.readline().strip()

main()