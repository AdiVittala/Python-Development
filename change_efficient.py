# Uses python3

change = 0
coins = 0

def get_change(money):
    global change
    global coins
    while money >= 10:
        quotient = money//10
        change = int(money%10)
        coins = coins+quotient
        money = change
    while money>=5:
        quotient = money//5
        change = int(money%5)
        coins = coins+quotient
        money = change
    while money>=1:
        quotient = money//1
        change = int(money%1)
        coins = coins+quotient
        money = change
    return coins

n = int(input())
print(get_change(n))
