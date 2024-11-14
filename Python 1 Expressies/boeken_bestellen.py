bookPrice = 24.95
discountPercentage = 40
n=60
shipmentCost = 3+(n-1)*0.75
cost = bookPrice *(100-discountPercentage)/100 * n
totalCost = shipmentCost+cost;
print(totalCost)