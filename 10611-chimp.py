from sys import stdin

def solve(ladies, x):
  aux1,aux2,ans = 1,1,[None,None]
  low,hi = 0,len(ladies)-1

  if(ladies[0] >= x):
    while(ladies[aux1]==x): aux1+=1
    return ['X',ladies[aux1]]

  if(ladies[-1] <= x):
    while(ladies[-aux2]==x): aux2+=1
    return [ladies[-aux2],'X']

  while(low+1 != hi):
    mid = low+((hi-low) >> 1)
    if(ladies[mid] == x ):
    	while(ans[0]==None or ans[1]==None):
    	    if(ladies[mid+aux1] == x): aux1+=1
    	    else: ans[1]=ladies[mid+aux1]
    	    if(ladies[mid-aux2] == x): aux2+=1
    	    else: ans[0]=ladies[mid-aux2]
    	return ans

    elif(ladies[mid] < x < ladies[mid+1]): return [ladies[mid],ladies[mid+1]]
    elif(ladies[mid-1] < x < ladies[mid]): return [ladies[mid-1],ladies[mid]]
    elif(x<ladies[mid]): hi = mid
    elif(x>ladies[mid]): low = mid

def main():
  inp = stdin
  inp.readline()
  ladies = [ int(x) for x in inp.readline().split() ]
  inp.readline()
  queries = [ int(x) for x in inp.readline().split() ]
  for x in queries:
    ans = solve(ladies, x)
    print(ans[0],ans[1])
main()
