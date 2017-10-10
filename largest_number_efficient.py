#Uses python3

def list_sort(a):
    sorted_digits = sorted(a, key=int, reverse=True)
    salary = int(''.join(map(str,sorted_digits)))
    return salary

def largest_number(n,a):
    global max_salary
    individual_digits = []
    single_digits = []
    ten_digits = []
    k = all(j>9 for j in a)
    while k:
        max_salary = list_sort(a)
        return max_salary
    for i in range(n):
        if a[i]>9:
            if a[i] == 10:
                ten_digits.append(a[i])
            else:
                number = a[i]
                digits = [int(x) for x in str(number)]
                individual_digits.extend(digits)
        else:
            single_digits.append(a[i])
    single_digits.extend(individual_digits)
    #print(single_digits)
    sorted_digits = sorted(single_digits, key=int, reverse=True)
    sorted_digits.extend(ten_digits)
    max_salary = int(''.join(map(str,sorted_digits)))
    return max_salary

max_salary = 0
n = int(input())
a = list(map(int, input().split()))
print(largest_number(n,a))
    
