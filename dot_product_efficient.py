#Uses python3

import sys

def max_dot_product(a, b):
    c = sorted(a, key=int, reverse=True)
    d = sorted(b, key=int, reverse=True)
    res = 0
    for i in range(len(c)):
        res += c[i] * d[i]
    return res


n = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(max_dot_product(a, b))
    
