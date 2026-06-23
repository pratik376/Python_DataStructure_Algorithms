def profitLoss(arr):

    min_val= float('inf')
    profit=0
    for val in arr:

        min_val= min(min_val, val)
        
        if val > min_val:
            profit+= val-min_val
            min_val=val

    return profit    

def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit