# Uses python3


def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here

    return value


data = list(map(int, input().split()))
n, capacity = data[0:2]
values = data[2:(2 * n + 2):2]
weights = data[3:(2 * n + 2):2]
#opt_value = get_optimal_value(capacity, weights, values)
#print("{:.10f}".format(opt_value))
print (n,capacity,values, weights)
