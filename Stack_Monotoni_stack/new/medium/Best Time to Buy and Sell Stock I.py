def profitLoss(arr):

    min_val= float('inf')
    profit= float('-inf')
    for val in arr:

        min_val= min(min_val, val)
        
        profit= max(profit, val-min_val)

    return profit    

