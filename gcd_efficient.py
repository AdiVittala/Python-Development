# Uses python3
#import sys

def gcd_efficient(number1,number2):
    if(number1<number2):
        remainder = number2%number1
        number2 = number1;
        number1 = remainder
        while(remainder !=0):
            remainder = number2%number1
            number2 = number1
            number1 = remainder
        return(number2)
    else:
        remainder = number1%number2
        number1 = number2;
        number2 = remainder
        while(remainder !=0):
            remainder = number1%number2
            number1 = number2
            number2 = remainder
        return(number1)

#input = sys.stdin.read()
a, b = map(int, input().split())
print(gcd_efficient(a, b))
