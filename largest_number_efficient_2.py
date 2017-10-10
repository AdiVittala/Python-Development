#Uses python3

def list_sort(a):
    inter_list = []
    sorted_list_reverse = sorted(a, key=int, reverse=True)
    for x in sorted_list_reverse:
        if x%10 == 0:
            inter_list.append(x)
            z = sorted_list_reverse.index(x)
            del sorted_list_reverse[z]
    new_list_reverse = sorted_list_reverse + inter_list
    sorted_list_forward = sorted(a, key=int)
    return (new_list_reverse, sorted_list_forward)

def largest_number(n,a):
    forward_string = ""
    reverse_string = ""
    reverse, forward = list_sort(a)
    for i in forward:
        forward_string += str(i)
    for j in reverse :
        reverse_string += str(j)
    forward_int = int(forward_string)
    reverse_int = int(reverse_string)
    if forward_int>=reverse_int:
        return forward_int
    else:
       return reverse_int

n = int(input())
a = list(map(int, input().split()))
print(largest_number(n,a))
    
