from sys import stdin
import sys
sys.setrecursionlimit(10000)

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
  cases = int(stdin.readline().strip())
  ans = "Optimal train swapping takes {} swaps."
  for i in range(cases):
    n = int(stdin.readline().strip())
    src = [int(i) for i in stdin.readline().split()]
    print(ans.format(solve(src,0,n)))

main()
