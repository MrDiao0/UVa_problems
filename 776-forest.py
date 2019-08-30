from sys import stdin
from collections import OrderedDict

deltar = [-1,-1,-1,0,0,1,1,1]
deltac = [-1,0,1,-1,1,-1,0,1]
visited = None

def maxCol(m):
	maxlen = []
	cnt = 0
	while(cnt < len(m[0])):
		tmp = 0
		for i in range(len(m)):
			if(m[i][cnt] > tmp): tmp = m[i][cnt]
		maxlen.append(tmp)
		cnt+=1
	return maxlen

def colLen(m):
	spaces,lens = [],maxCol(m)
	for i in lens:
		if i<10: spaces.append(1)
		elif i<100: spaces.append(2)
		elif i<1000: spaces.append(3)
		elif i<10000: spaces.append(4)
		elif i<100000: spaces.append(5)
	return spaces

def dfs(row,col,num,aux):
    global visited,ans,rows,cols
    stack = [ (row, col) ] ; visited[row][col] = 1
    while len(stack) != 0:
        r,c = stack.pop()
        for i in range(len(deltar)):
            dr,dc = r+deltar[i],c+deltac[i]
            if 0<=dr<rows and 0<=dc<cols and aux[row][col] == aux[dr][dc] and visited[dr][dc]==0 :
            	stack.append((dr,dc)); visited[dr][dc] = 1
            	ans[dr][dc] = num
        visited[r][c] = 2


def solve(n):
	global visited,ans,rows,cols
	visited = [[0 for _ in range(cols)] for _ in range(rows)]
	ans = [[0 for _ in range(cols)] for _ in range(rows)]
	num = 0
	for r in range(rows):
		for c in range(cols):
			if(visited[r][c] == 0):
				num+=1
				ans[r][c] = num
				dfs(r,c,num,n)
	return ans

def main():
	global rows,cols
	aux,n = stdin.readline().split(),[]
	while(len(aux)!=0):
		n.append(aux)
		aux = stdin.readline().split()
		if(len(aux)==0 or aux[0]=='%'):
			rows,cols = len(n),len(n[0])
			ans = solve(n)
			cLen = colLen(ans)

			for i in range(len(ans)):
				c = 0
				for j in range(len(ans[i])):
					if c == 0: print(str(ans[i][j]).rjust(cLen[j]),end = ''); c=1
					else: print(str(ans[i][j]).rjust(cLen[j]+1),end = '')
				print()
			print('%')
			n = []
			if(len(aux)!=0): aux = stdin.readline().split()

main()