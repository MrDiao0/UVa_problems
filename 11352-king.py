from sys import stdin
from collections import deque

deltar = [-1,-1,-1,0,0,1,1,1]
deltac = [-1,0,1,-1,1,-1,0,1]

elimr = [-2,-2,-1,-1,1,1,2,2]
elimc = [1,-1,2,-2,2,-2,1,-1]

def bfs(src,tgt):
    global visited,rows,cols,board
    row,col = src
    stack = deque([[row, col,1]]) ; visited[row][col] = 1
    while len(stack) != 0:
        r,c,cnt = stack.popleft()
        for i in range(len(deltar)):
            dr,dc = r+deltar[i],c+deltac[i]
            if 0<=dr<rows and 0<=dc<cols and visited[dr][dc]==0 :
            	stack.append((dr,dc,cnt+1)); visited[dr][dc] = 1
            	board[dr][dc] = cnt
            if(dr == tgt[0] and dc == tgt[1]): return cnt
        visited[r][c] = 2
    return -1

def main():
	global visited,rows,cols,board
	cases = int(stdin.readline().strip())
	while(cases>0):
		board = []
		rows,cols = map(int,stdin.readline().split())
		visited = [[0 for _ in range(cols)] for _ in range(rows)]
		
		for i in range(rows):
			aux,auxc = [],0
			for j in stdin.readline().strip():
				
				if(j=='.'): aux.append(0)
				if(j=='Z'):
					visited[i][auxc] = 1
					aux.append('Z')
					for m in range(8):
						if(0<=(i+elimr[m])<rows and 0<=(auxc+elimc[m])<cols):
							visited[i+elimr[m]][auxc+elimc[m]] = -1
				if(j=='A'): source = [i,auxc]; aux.append('A')
				if(j=='B'): target = [i,auxc]; aux.append('B')
				auxc += 1
			board.append(aux)
		visited[source[0]][source[1]] = 0
		visited[target[0]][target[1]] = 0
		ans = bfs(source,target)
		if ans == -1: print("King Peter, you can't go now!")
		else: print("Minimal possible length of a trip is {}".format(ans))
		cases-=1


main()