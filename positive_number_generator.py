#Uses Python 3
#Fix smallest number input = 1 exception. 
#Add exception and input value for x again

def positive_number_generator():

    import random
    x = int(input("Enter number of positive numbers to generated:"))
    file = open('random_number_file.txt','a')

    for count in range(x):
        num = random.randint(1,x)
        file.write(str(num)+ ' ')
    file.close()
    print('Random numbers generated to the file random_number_file.txt')


positive_number_generator()
