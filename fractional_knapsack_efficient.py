# Uses python3


def get_optimal_value(capacity, weights, values):
    value = 0
    full_capacity = 0
    inter_value = 0
    items_in_sack = 0
    value_per_weight = []
    remaining_capacity = capacity
    for items in range(n):
        quotient = float(values[items]/weights[items])
        value_per_weight.append(quotient)
    while full_capacity < capacity and items_in_sack<n:
        max_value = max(value_per_weight)
        max_index = value_per_weight.index(max_value)
        del value_per_weight[max_index]
        if weights[max_index]<=remaining_capacity:
            inter_value = float(max_value * weights[max_index])
            full_capacity = float(full_capacity + weights[max_index])
            value=float(value+inter_value)
        else:
            inter_value =float(max_value * remaining_capacity)
            full_capacity = float(full_capacity + remaining_capacity)
            value = float(value + inter_value)
        del weights[max_index]
        del values[max_index]
        remaining_capacity = float(capacity - full_capacity)
        items_in_sack +=1
    return value


values = []
weights = []
data = list(map(int, input().split()))
n, capacity = data[0:2]
for i in range(n):
    v,w = map(int, input().split())
    values.append(v)
    weights.append(w)
#values = data[2:(2 * n + 2):2]
#weights = data[3:(2 * n + 2):2]
opt_value = get_optimal_value(capacity, weights, values)
print("{0:.4f}".format(opt_value))

