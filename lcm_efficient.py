# Uses python3
#import sys

def lcm_efficient(number1,number2):
    product = int(number1*number2)
    if(number1<number2):
        remainder = number2%number1
        number2 = number1;
        number1 = remainder
        while(remainder !=0):
            remainder = number2%number1
            number2 = number1
            number1 = remainder
        lcm = int(product//number2)
        return(lcm)
        
    else:
        remainder = number1%number2
        number1 = number2;
        number2 = remainder
        while(remainder !=0):
            remainder = number1%number2
            number1 = number2
            number2 = remainder
        lcm = int(product//number1)
        return(lcm)

#input = sys.stdin.read()
a, b = map(int, input().split())
print(lcm_efficient(a, b))
