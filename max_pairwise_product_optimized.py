#Uses Python 3

import heapq
import positive_number_generator

with open('random_number_file.txt','r') as fread:
   for line in fread:
       numbers_int = map(int,line.split())

max_numbers = heapq.nlargest(2,numbers_int)
max_product = max_numbers[0]*max_numbers[1]
print("Maximum Pairwise Product:", max_product)
