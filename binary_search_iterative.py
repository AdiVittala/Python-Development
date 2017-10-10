# Uses python3
import math

def binary_search(a,low,high,x):
    while low<=high:
        mid_original = low + ((high - low)/2)
        mid_floor = math.floor(mid_original)
        if x == a[mid_floor]:
            return mid_floor
        elif x < a[mid_floor]:
            high = mid_floor - 1
        else:
            low = mid_floor + 1
    return -1
       

data = list(map(int, input().split()))
data1 = list(map(int, input().split()))
n = data[0]    
a = data[1 : n + 1]
k = data1[0]
b = data1[1:k+1]
left, right = 0, len(a)-1

for x in b:
    print(binary_search(a,left,right,x),end=" ")
