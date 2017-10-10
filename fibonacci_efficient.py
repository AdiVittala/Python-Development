# Uses python3

fib_list = []

def fib_generator(number):
    fib_list.append(0)
    fib_list.append(1)
    if number == 0:
        return(0)
    elif number == 1:
        return(1)
    else:
        for count in range(2,number+1) :
            value = fib_list[count-2]+fib_list[count-1]
            fib_list.append(value)
        return(fib_list[number])
    
#n = int(input("Enter number whose Fibonacci number needs to be generated:"))
n = int(input())
#k = fib_generator(n)
#print('Fibonacci number of %d is %d' %(n,k))
print(fib_generator(n))


