def continuousSubArray(arr,k):

    reminder= {0,-1}

    prefix=0


    for i,num in enumerate(arr):
        prefix+= num

        if k!=0:
            prefix %= k

        if prefix in reminder:

            if i- reminder[prefix] > 1:
             return True
        else:
           reminder[prefix]=i 

    return False          


