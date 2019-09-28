#UVa: 10327 - Flip sort
from sys import setrecursionlimit as SRL
from sys import stdin
SRL(10000)

def solve(num, low, hi):
  r = 0  
  if( hi-low<=1 ):
    return 0
  mid = low+((hi-low) >> 1)
  aux,a,b = [],low,mid

  r = solve(num,low,mid)
  r += solve(num,mid,hi)

  while( a < mid and  b < hi):
    if( num[a] <= num[b]):
      aux.append(num[a])
      a += 1
    elif( num[a] > num[b]):
      aux.append(num[b])
      b += 1
      r += mid - a
  
  while( a < mid):
    aux.append(num[a])
    a += 1
  
  while( b < hi):
    aux.append(num[b])
    b += 1

  num[low:hi] = aux
  return r

def main():
  n = stdin.readline().strip()
  lab = "Minimum exchange operations : {}"
  while len(n):
    num = list(map(int,stdin.readline().split()))
    print(lab.format(0 if 0<=int(n)<=1 else solve(num, 0, len(num))))
    n = stdin.readline().strip()

main()