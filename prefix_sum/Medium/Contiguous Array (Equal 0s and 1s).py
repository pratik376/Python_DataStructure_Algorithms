def contiguousArray(arr):

    my_dict= {0:1}
    currSum=0
    res= float('-inf')

    arr= [-1 if num==0 else 1 for num in arr]   
    for i, elemnt in enumerate(arr):

        currSum+=elemnt

       # diff=elemnt-0

        if currSum in my_dict:
            res= max(res, i-my_dict[currSum])
        else:    
         my_dict[currSum]= i

    return res     



  