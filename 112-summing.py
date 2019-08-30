import sys
from sys import stdin
sys.setrecursionlimit(10000)

def solve(T,n):
	global is_in,a
	if not len(T[1]) and not len(T[2]):
		if a == n+T[0]: is_in = True
	else:
		if len(T[1]): l = solve(T[1],n+T[0])
		if len(T[2]): r = solve(T[2],n+T[0])
	return

def next_N():
	global i, INPUT
	while ((not INPUT[i].isdigit()) and (not INPUT[i]=='-')) and INPUT[i]!=')': i+=1
	if INPUT[i]==')':
		ans = None

	elif INPUT[i]!=')':
		j=i+1
		while j<len(INPUT) and (INPUT[j].isdigit() or INPUT[j]=='-'):
			j+=1
		ans = int(INPUT[i:j])
		i=j
	
	return ans

def parse():
	global i,INPUT
	Tree = []
	n = next_N()
	if n != None:
		Tree = [n]

		while INPUT[i]!='(': i += 1
		Tree.append(parse()) #left

		while INPUT[i]!='(': i += 1
		Tree.append(parse()) #right

	return Tree

def main():
	global i,INPUT,is_in,a
	i = 0
	INPUT = stdin.read()
	while i<len(INPUT):

		is_in = False
		a = next_N()
		T = parse()
		if len(T):
			solve(T,0)
			if is_in == True: print("yes")
			else: print("no")

		else: print("no")
		while i<len(INPUT) and not (INPUT[i].isdigit() or INPUT[i]=='-') and INPUT[i]!='(': i+=1

main()