# Uses python3

import sys

def optimal_sequence(n):
    if n==1:
        return[1]
    operations = min_operations(n)
    return min_list(n, operations)

def min_list(n, operations):
    sequence = []
    while n>0:
        sequence.append(n)
        if n%2 !=0 and n%3 !=0:
            n = n-1
        elif n%2 == 0 and n%3 == 0:
            n = n//3
        elif n%2 == 0:
            if operations[n-1] < operations[n//2]:
                n = n-1
            else:
                n = n//2
        elif n%3 == 0:
            if operations[n-1] < operations[n//3]:
                n = n-1
            else:
                n = n//3
        return reversed(sequence)

def min_operations(n):
    result = []
    for i in range(0, n+1):
        result.append(0)
    for i in range(2, n+1):
        min1 = result[i-1]
        min2 = sys.maxsize
        min3 = sys.maxsize
        if i%2 == 0:
            min2 = result[int(i/2)]
        if i%3 == 0:
            min3 = result[int(i/3)]
        minoperations = min(min1,min2,min3)

        result[i] = minoperations+1
    return result
    
input1 = sys.stdin.read()
n = int(input1)
sequence = list(optimal_sequence(n))
print(len(sequence)-1)
for x in sequence:
    print(x, end= ' ')



