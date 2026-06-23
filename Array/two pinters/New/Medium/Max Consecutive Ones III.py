def consecutives(arr,k):

    l,r=0
    max_length=0
    

    while r< len(arr):

        if (arr[r]==0 and k):
            k-=1
        elif (arr[r]==0 and k==0):

            max_length=max(max_length, r-l)
            while(arr[l]!=0):
                l+=1
            k+=1
            l+=1

            continue
        r+=1

    return max(max_length, r-l+1)            


def consecutives(arr,k):

    l,r=0
    max_length=0
    zero_count=0
    

    while r< len(arr):

        if (arr[r]==0):
            zero_count+=1
        
        while zero_count >k:
            if arr[l]==0:
                zero_count-=1
            l+=1    

        max_length=max(max_length,r-l+1)

        r+=1

    return max_length    

           
           

       