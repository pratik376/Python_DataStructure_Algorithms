def missingNumber(arr):

    n= len(arr)
    total_sum= (n * (n+1) ) //2

    missing_num= total_sum - sum(arr)

    return missing_num



