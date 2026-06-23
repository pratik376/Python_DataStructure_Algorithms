def makeArrayNonDecreasing(arr):

    stack=[]


    for i in range(len(arr)):

        if not stack or arr[i] >= stack[-1]:
            stack.append(arr[i])


    return len(stack)        


def makeArrayNonDecreasing(arr):

    count=0
    max_val= float('-inf')


    for i in range(len(arr)):

        if arr[i] > max_val:
            max_val=arr[i]
            count+=1

    return count        

     