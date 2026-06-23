def count(arr):

    n= len(arr)

    i=1
    count=0
    left, right= 0,0

    while i < n-1:

        left= i-1
        right= i+1

        while left >=0 and arr[i] == arr[left] :
            left-=1

      
        while right <n and arr[i] == arr[right] :
            right+=1

        
        if left >=0 and right < n:

            if ((arr[i]> arr[left] and arr[i]> arr[right]) or 
            (arr[i]< arr[left] and arr[i]< arr[right] )):
             count+=1
        
        i=right

    return count                

        
