def maxProfit(prices):
    i = 0
    maxp = 0
    for j in range(1,len(prices)):
        if prices[j] >= prices[i]:
            maxp = (prices[j]-prices[i]) + maxp
            i= j
        else:
            i+=1
    return maxp

prices = [7,1,5,3,6,4]
print(maxProfit(prices))