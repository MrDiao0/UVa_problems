#UVa: 10810 - Ultra-QuickSort
from sys import setrecursionlimit as SRL
from sys import stdin
SRL(10000)

def mergeSort(nums, lo, hi):
  ans = 0  
  if( hi-lo<=1 ):
    return 0
  mid = lo+((hi-lo) >> 1)
  aux,a,b = [],lo,mid

  ans = mergeSort(nums,lo,mid)
  ans += mergeSort(nums,mid,hi)

  while( a < mid and  b < hi):
    if( nums[a] <= nums[b]):
      aux.append(nums[a])
      a += 1
    elif( nums[a] > nums[b]):
      aux.append(nums[b])
      b += 1
      ans += mid - a
  
  while( a < mid):
    aux.append(nums[a])
    a += 1
  
  while( b < hi):
    aux.append(nums[b])
    b += 1

  nums[lo:hi] = aux
  return ans

def main():
  n = int(stdin.readline())
  while n:
    l = list()
    for e in range(n):
      l.append(int(stdin.readline()))
    print(mergeSort(l,0,n))
    n = int(stdin.readline())

main()