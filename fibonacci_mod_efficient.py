# Uses python3

period_list = []
fib_list = []
period = 0

def fib_period(modulo):
    global period
    period_list.append(0)
    period_list.append(1)
    if modulo == 0:
        return(0)
    elif modulo== 1:
        return(1)
    else:
        limit = int(modulo*modulo)
        for count in range(2,limit+1):
            value = (period_list[count-2]+period_list[count-1])%modulo
            period_list.append(value)
            if period_list[count-1] == 0 and period_list[count] == 1:
                period = count-1
                break
        return(period)

def fib_huge(number,divide):
    fib_list.append(0)
    fib_list.append(1)
    if number == 0:
        return(0)
    elif number== 1:
        return(1)
    else:
        for tracker in range(2,number+1):
            value1 = (fib_list[tracker-2]+fib_list[tracker-1])%divide
            fib_list.append(value1)
        return(fib_list[number])



n, m = map(int, input().split())

p = fib_period(m)
remainder = n%p

print(fib_huge(remainder,m))
