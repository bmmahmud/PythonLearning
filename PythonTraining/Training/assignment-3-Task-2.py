# Assignment - 3 Task - 2 [B.M. ASHIK MAHMUD]
# Task 02: Create two list named as Actual Price and Tax with five different products.
# Then calculate each products sales price.
# You could show the results as a single list.
# Remember, you have to use loop.

actualPrice = [12,20,16,40,35]
tax = [2,2.5,1.7,4,3.2]
newlist = []
for x in range(len(actualPrice)):
    sumation = actualPrice[x]+tax[x]
    newlist.append(sumation)

print('Product price with Tax:',newlist)





