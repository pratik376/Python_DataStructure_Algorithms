def valid_triangle(arr):

    arr.sort()

    n= len(arr)

    count=0

    for i in (n-1,1, -1):

        left, right= 0, i-1

        while left<right:

            if arr[left]+arr[right]> arr[i]:

                count+= right-left
                right-=1


            else:    
                left+=1

    return count            

