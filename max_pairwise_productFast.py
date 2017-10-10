#Uses Python 3

import heapq
#import positive_number_generator
import random
def positive_number_generator():
    n = int(input())
    a = [int(x) for x in input().split()]
    #x = int(input("Enter number of positive numbers to generated:"))
    #file = open('random_number_file.txt','a')
    #for count in range(n):
     #   num = random.randint(1,n)
     #   file.write(str(num)+ ' ')
    #file.close()
    #print('Random numbers generated to the file random_number_file.txt')
    return a

numbers_int = positive_number_generator()

#with open('random_number_file.txt','r') as fread:
   # for line in fread:
   #     numbers_int = map(int,line.split())

#max_numbers = heapq.nlargest(2,numbers_int)
max_numbers = heapq.nlargest(2,numbers_int)
max_product = max_numbers[0]*max_numbers[1]
print(max_product)
#print("Maximum Pairwise Product:", max_product)
