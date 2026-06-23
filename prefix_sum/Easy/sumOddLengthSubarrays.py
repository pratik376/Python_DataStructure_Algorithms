def sumOddLengthArray(arr):

    total=0
    n=len(arr)

    for i, val in enumerate(arr):

        odd_cont= ((i+1) * (n-i) ) //2
        total += val * odd_cont

    return total    

