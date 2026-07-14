def maxProfit(prices):
    i = 0
    pft = 0
    for j in range(1,len(prices)):
        if prices[j] >= prices[i]:
            pft = (prices[j]-prices[i]) + pft
            i= j
            
        else:
            i+=1
    return pft

prices = [7,1,5,3,6,4]
print(maxProfit(prices))