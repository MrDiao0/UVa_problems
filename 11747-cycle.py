#UVa 11747 - Heavy Cycle Edges
from sys import stdin

class dforest(object):
  """implements an union-find with path-compression and ranking"""

  def __init__(self, size=10):
    self.__parent = [ i for i in range(size) ]
    self.__rank = [ 1 for _ in range(size) ]
    self.__csize = [ 1 for _ in range(size) ]

  def __str__(self):
    """return the string representation of the forest"""
    return str(self.__parent)

  def __len__(self):
    """return the number of elements in the forest"""
    return self.__size
  
  def find(self, x):
    """return the representative of the component of x"""
    if self.__parent[x]!=x:
      self.__parent[x] = self.find(self.__parent[x])
    return self.__parent[x]
  
  def union(self, x, y):
    """computes the union of the components of x and y, if they are different"""
    fx,fy = self.find(x),self.find(y)
    if fx!=fy:
      rx,ry = self.__rank[fx],self.__rank[fy]
      if rx>ry:
        self.__parent[fy] = fx
        self.__csize[fx] += self.__csize[fy]
      else:
        self.__parent[fx] = fy
        self.__csize[fy] += self.__csize[fx]
        if rx==ry:
          self.__rank[fy] += 1

def kruskal(graph, lenv):
  ans = list()
  graph.sort(key = lambda x: x[2])
  #print(graph)
  df,i = dforest(lenv),0
  while i!=len(graph):
    u,v,d = graph[i]
    if df.find(u)!=df.find(v):
      df.union(u, v)
    else:
      ans.append(d)
    i += 1
  return ans
    
def main():
  n,m = map(int,stdin.readline().split())
  while n+m:
  	G = list()
  	for _ in range(m):
  		u,v,w = map(int,stdin.readline().split())
  		G.append((u,v,w))

  	ans = kruskal(G,n)
  	if len(ans):
  		for u in range(len(ans)):
  			if u<len(ans)-1: print(ans[u],end=' ')
  			else: print(ans[u])
  	else:
  		print("forest")

  	n,m = map(int,stdin.readline().split())
  
main()