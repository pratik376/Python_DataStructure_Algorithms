def binarySubArray(arr, goal):

    table= {0:1}

    currSum=0

    res=0

    for num in range(len(arr)):

        currSum+=arr[num]

        diff= currSum-goal

        res+= table.get(diff,0)

        table[currSum]= 1+ table.get(currSum,0)

    return res    





