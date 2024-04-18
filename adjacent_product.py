from time import time

def adjacentElementProduct(inputarray):
    largest_product = 0
    for i in range(1,len(inputarray)):
        product = inputarray[i] * inputarray[i -1]
        if product > largest_product:
            largest_product = product
    return largest_product

array = [3, 6, -2, -5, 7, 3]

max = adjacentElementProduct(array)



print(max)
