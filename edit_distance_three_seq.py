#Uses python3

import sys

def edit_distance(a, b, c):
    dp_result = [[[0 for k in range(l+1)] for j in range(m+1)] for i in range(n+1)]

    for x in range(1, n+1):
        for y in range(1, m+1):
            for z in range(1, l+1):
                if a[x-1] == b[y-1] and b[y-1] == c[z-1]:
                    dp_result[x][y][z] = dp_result[x-1][y-1][z-1] + 1
                else: 
                    dp_result[x][y][z] = max(dp_result[x-1][y][z], dp_result[x][y-1][z], dp_result[x][y][z-1])

    return dp_result

def lcs3(a, b, c):
    return edit_distance(a,b,c)



n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
l = int(input())
c = list(map(int, input().split()))
result = lcs3(a, b, c) 
print(result[n][m][l])
