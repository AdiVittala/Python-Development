# Uses python3

def fib_huge(number):
    global last_digit
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
        last_digit = int(remainder_sum%10)
        return(last_digit)
       
n = int(input())
remainder = n%60
fib_list = []
last_digit = 0

print(fib_huge(remainder))

