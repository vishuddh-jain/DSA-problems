def maxProfit(prices):

    i = 0
    n = len(prices)
    max_profit = 0

    for j in range(1,n) :
        if prices[j] >= prices[i] :
            max_profit = max(prices[j] - prices[i], max_profit)
        else :
            i = j
    return max_profit        
prices = [6,2,3,5,1,2]
print(maxProfit(prices))