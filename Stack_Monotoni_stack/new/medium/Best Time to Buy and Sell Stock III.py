def profitLoss(arr):

    min_val= float('inf')
    profit=0
    for val in arr:

        min_val= min(min_val, val)
        
        if val > min_val:
            profit+= val-min_val
            min_val=val

    return profit    
