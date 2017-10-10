# Uses python3
import math

def my_counter(a, left, right, maj_element):
    my_count = 0
    for i in range(left, right+1):
        if a[i] == maj_element:
            my_count += 1
    return my_count

def get_majority_element(a, left, right):
    if left>right:
        return -1
    if left==right:
        return a[left]
    mid_original = left + ((right-left)/2)
    mid_floor = math.floor(mid_original)
    leftA = get_majority_element(a, left, mid_floor)
    rightA = get_majority_element(a, mid_floor+1, right)
    if leftA == -1 and rightA != -1:
        num = my_counter(a, left, right, rightA)
        if num > (right - left +1)/2:
            return rightA
        else:
            return -1
    elif rightA == -1 and leftA != -1:
        num = my_counter(a, left, right, leftA)
        if num > (right - left +1)/2:
            return leftA
        else:
            return -1
    elif leftA != -1 and rightA != -1:
        left_num = my_counter(a, left, right, leftA)
        right_num = my_counter(a, left, right, rightA)
        if left_num > (right -left +1)/2:
            return leftA
        elif right_num > (right - left+1)/2:
            return rightA
        else:
            return -1
    else:
        return -1

        


n = int(input())
a = list(map(int, input().split()))
right_index = n-1

if get_majority_element(a, 0, right_index) != -1:
    print(1)
else:
    print(0)
