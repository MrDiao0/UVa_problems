#UVa: 13055 - Inception
from sys import stdin

def main():
	cases = int(stdin.readline())
	dream = list()
	for _ in range(cases):
		line = stdin.readline().split()
		if line[0]=='Sleep':
			dream.append(line[1])
		elif line[0]=='Test':
			if len(dream): print(dream[-1])
			else: print("Not in a dream")
		elif line[0]=='Kick':
			if len(dream): dream.pop()

main()