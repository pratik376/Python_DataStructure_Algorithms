def niceSubarray(arr,k):

    # we have converted this problem to subarraysum equals to k

    currum=0
    mydict= {0:1}
    res=0

    odd_count= [1 if num%2==1 else 0  for num in arr]

    for num in odd_count:

        currum+= num
        diff= currum-k

        res+= mydict.get(diff,0)

        mydict[currum] = 1+ mydict.get(currum,0)

    return    res 



        


        
