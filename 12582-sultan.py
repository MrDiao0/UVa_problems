from sys import stdin
from collections import deque

def mergesort(num,low,hi):
  r = 0  
  if( hi-low<=1 ):
    return 0
  mid = low+((hi-low) >> 1)
  aux,a,b = [],low,mid

  r = mergesort(num,low,mid)
  r += mergesort(num,mid,hi)

  while( a < mid and  b < hi):  
    if( num[a][0] <= num[b][0]):
      aux.append(num[a])
      a += 1
    elif( num[a][0] > num[b][0]):
      aux.append(num[b])
      b += 1
  while( a < mid):
    aux.append(num[a])
    a += 1
  
  while( b < hi):
    aux.append(num[b])
    b += 1
  num[low:hi] = aux
  r+=1
  if(r == len(num)-1):
  	return num
  return r

def solve(src):
  queue,aux = deque(),[]
  queue.append([src[0]])
  if(len(src) == 2): return [[src[0],0]]

  for i in range(1,len(src)-1):
    tmp = queue.pop()

    if(src[i] != tmp[0]):
      queue.append(tmp); queue.append([src[i]])
    else:
      tmp2 = tmp
      tmp = queue.pop()
      tmp.append(src[i]); queue.append(tmp)
      if(tmp[0] != tmp2[0]): aux.append(tmp2)
  
  tmp.pop()
  aux.append(tmp)
  #aux.append(tmp[0:len(tmp)-1])
  ans = mergesort([[i[0],len(i)] for i in aux],0,len(aux))
  return ans

def main():
  n = int(stdin.readline().strip())
  for i in range(n):
    src = stdin.readline().strip()
    ans = solve(src)
    print("Case",i+1)
    for j in ans: print(j[0],'=',j[1])

main()