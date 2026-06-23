def productArray(arr):

    prefix=[1]* len(arr)
    suffix= [1] * len(arr)
    answer= [1] * len(arr)

    currProduct=1

    for i in range(1, len(arr)):
        currProduct*=arr[i-1]
        prefix[i]= currProduct

    currProduct=1

    for  i in range(len(arr)-2, -1,-1):
        currProduct*= arr[i+1]
        suffix[i]=  currProduct

    for i in range(len(arr)):

        answer[i]= suffix[i] * prefix[i]

    return answer    



    
arr=[1,2,3,4]

print(productArray(arr))  # o(n) space  0(n) time




def productArray(arr):
    n= len(arr)
    answer=[1] * n

    prefix=1

    for  i in range(n):

        answer[i]= prefix
        prefix *= arr[i]

    suffix=1

    for i in range(n-1,-1,-1):

        answer[i]*= suffix
        suffix*= arr[i]     

    return answer    