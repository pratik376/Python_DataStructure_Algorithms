def divisonSubarray(arr, k):

    divisions={0:1}
    res=0
    currSum=0

    for i in range(len(arr)):

        currSum+= arr[i]

        if k !=0:
            currSum%=k

        res+= divisions.get(currSum,0)

        divisions[currSum]=1+ divisions.get(currSum,0)

    return res        

