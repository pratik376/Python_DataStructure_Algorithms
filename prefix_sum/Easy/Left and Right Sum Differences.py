def left_right_difference(arr):

    postfix=[0]* (len(arr)+1)
    prefix=[0]* (len(arr)+1)
    output=[]

    for i in range(len(arr)):
        prefix[i+1]=prefix[i]+arr[i]

    for j in range(len(arr)-1,-1,-1):

        postfix[j]= arr[j]+ postfix[j+1]

    for k in range(len(arr)):

        output.append(abs(prefix[k]- postfix[k+1]))

    return output    


def left_right_difference(arr):

    output=[]

    left_sum=0
    right_sum= sum(arr)

    for i in range(len(arr)):

        right_sum-= arr[i]

        output.append(abs(left_sum-right_sum))

        if i < len(arr)-1:  
          left_sum+=arr[i] 

    return output    

        

    

arr=[10,4,8,3]

left_right_difference(arr)


