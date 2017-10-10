# Uses python3

def fib_huge(number):
    global remainder_sum
    global fib_list
    remainder_sum = 0
    fib_list = []
    fib_list.append(0)
    fib_list.append(1)
    if number == 0:
        return(0)
    elif number== 1:
        return(1)
    else:
        for tracker in range(2,number+1):
            value1 = (fib_list[tracker-2]+fib_list[tracker-1])%10
            fib_list.append(value1)
        remainder_sum = sum(fib_list)
        #last_digit = int(remainder_sum%10)
        return(remainder_sum)
       
n, m = map(int, input().split())
remainder = int(n%60)
high_remainder = int(m%60)
actual_remainder = int(remainder-1)
fib_list = []
remainder_sum = 0

k = fib_huge(actual_remainder)
q = fib_huge(high_remainder)
first_answer = int(q-k)
final_answer = int(first_answer%10)
print(final_answer)
