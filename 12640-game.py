#UVa: 12640 - Largest Sum Game
from sys import stdin

def main():
	line = stdin.readline().split()
	while len(line):
		nums = list(map(int,line))

		ans,cnt = 0,0
		for u in nums:
			cnt += u
			ans = max(ans,cnt)
			cnt = max(cnt,0)
		print(ans)
		line = stdin.readline().split()

main()