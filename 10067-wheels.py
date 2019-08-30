from sys import stdin
from collections import deque

def f0(n): return n//1000
def f1(n): return (n - (n//1000)*1000)//100
def f2(n): return (n-(n//100)*100)//10
def f3(n): return (n- (n//10)*10)

def adjacents():
    global adj
    delta = [(0,0,0,1),(0,0,1,0),(0,1,0,0),(1,0,0,0),(0,0,0,-1),(0,0,-1,0),(0,-1,0,0),(-1,0,0,0)]
    aux = []

    for e in range(10000):
        for x,y,z,w in delta:
            pos = [x + f0(e),y + f1(e),z + f2(e), w + f3(e)]
            for i in range(4):
                if(pos[i] == -1): pos[i] = 9
                elif (pos[i] == 10): pos[i] = 0
                else: pos[i] = pos[i]
            aux1 = pos[0]*1000 + pos[1]*100 + pos[2]*10 + pos[3]
            aux.append(aux1)
        print(aux)
        adj.append(aux)
        aux = []
    return

def bfs(source,target,visited):
    global adj

    if(visited[target] == -1 or visited[source] == -1): return -1

    queue = deque()
    queue.append(source)

    while(len(queue)!=0):
        u = queue.popleft()
        if u == target: return visited[target]
        for i in range(8):
            next2 = adj[u][i]
            if(visited[next2] == 0):
                visited[next2] = visited[u] + 1
                queue.append(next2)

    return -1

def main():
    global adj
    adj = []
    cases = int(stdin.readline().strip())
    adjacents()

    for _ in range(cases):
        vis = [0 for _ in range(10000)]
        empty = stdin.readline()
        src = int(stdin.readline().strip().replace(' ',''))
        tgt = int(stdin.readline().strip().replace(' ',''))
        cases = int(stdin.readline())

        for i in range(cases):
            delete = int(stdin.readline().strip().replace(' ',''))
            vis[delete] = -1
        
        print(bfs(src,tgt,vis))

main()