# Uses python3
import math

def binary_search(a,low,high,x):
    l_boundary, r_boundary = 0, len(a)-1
    #print (l_boundary,r_boundary)
    #print(low,high)
    if low > r_boundary or high < l_boundary:
        return -1
    mid_orginal = low + ((high-low)/2)
    mid_floor = math.floor(mid_orginal)
    #print(mid_floor)
    if x == a[mid_floor]:
        return mid_floor
    elif x<a[mid_floor]:
        return binary_search(a,left,mid_floor-1,x)
    else:
        return binary_search(a,mid_floor+1,right,x)

data = list(map(int, input().split()))
data1 = list(map(int, input().split()))
n = data[0]    
a = data[1 : n + 1]
k = data1[0]
b = data1[1:k+1]
left, right = 0, len(a)
#print (n,a,k,b)
#print (left,right)

for x in b:
    # replace with the call to binary_search when implemented
    print(binary_search(a,left,right,x),end=" ")
