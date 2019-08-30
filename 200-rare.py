from sys import stdin

def repeated(n,l):
  for i in l:
    if(n==i): return True
  return False

def toposort(G):
  indeg = [-1 for _ in range(len(G))]
  n = 0
  for u in range(len(G)):
    if(len(G[u])>0):
      if(G[u][0]>=0 and indeg[u]==-1): indeg[u] = 0; n+=1
      for v in G[u]:        
        if(indeg[v] == -1): indeg[v] = 0; n+=1
        indeg[v] += 1
  topo = []

  while len(topo)<n:
    for i in range(len(G)):
      if indeg[i]!=-1:
        if indeg[i] == 0:
          
          topo.append(chr(i+64))
          
          for j in G[i]:
            indeg[j] -= 1
          indeg[i] = -1
  return topo

def solve(n):
  global maxlen
  if maxlen==1: return [i for i in n]
  edgeL = []
  Graph = [[] for _ in range(27)]
  G = [[0 for _ in range(maxlen+1)] for _ in range(len(n))]
  for i in range(len(n)):
    for j in range(len(n[i])):
      G[i][j] = ord(n[i][j])-64
  for r in range(len(n)-1):
    stop = False
    cnt = 0
    while(not stop):
      if(G[r][cnt]==0 or G[r+1][cnt]==0): stop = True
      elif(G[r][cnt]==G[r+1][cnt]): cnt+=1
      elif(G[r][cnt]!=G[r+1][cnt]): 
        
        if(not repeated(G[r+1][cnt],Graph[G[r][cnt]])):
          Graph[G[r][cnt]].append(G[r+1][cnt]); stop = True
        else: stop = True
  return toposort(Graph)

def main():
  global maxlen
  aux = stdin.readline().strip()
  while(len(aux)>0):
    N = []
    maxlen = 0
    while(aux!='#'):
      if(len(aux) > maxlen): maxlen = len(aux)
      N.append(aux)
      aux = stdin.readline().strip()
    [print(i,end='') for i in solve(N)]
    print()
    aux = stdin.readline().strip()

main()