#UVa 10034 - Freckles
from sys import stdin
from math import sqrt

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
  ans = 0
  graph.sort(key = lambda x: x[2])
  df,i = dforest(lenv),0
  while i!=len(graph):
    u,v,d = graph[i]
    if df.find(u)!=df.find(v):
      ans += d
      df.union(u, v)
    i += 1
  return ans

def main():
	cases = int(stdin.readline())
	empty = stdin.readline()

	for i in range(cases):
		coords = list()
		n = int(stdin.readline())
		for u in range(n):
			x,y = map(float,stdin.readline().split())
			coords.append((x,y))

		G = list()
		for a in range(len(coords)):
			for b in range(a+1,len(coords)):
				if coords[a][1]>=coords[b][1]:
					c1 = coords[a][1] - coords[b][1]
				elif coords[b][1]>coords[a][1]:
					c1 = coords[b][1] - coords[a][1]

				if coords[a][0]>= coords[b][0]:
					c2 = coords[a][0] - coords[b][0]
				elif coords[b][0]>coords[a][0]:
					c2 = coords[b][0] - coords[a][0]
				
				if coords[a][0] == coords[b][0]:
					G.append((a,b,c1))
				elif coords[a][1] == coords[b][1]:
					G.append((a,b,c2))
				else:
					w = sqrt(pow(c1,2)+pow(c2,2))
					G.append((a,b,w))

		ans = kruskal(G,n)
		print("{:.2f}".format(ans))
		if i<cases-1: print()
		
		empty = stdin.readline()

main()