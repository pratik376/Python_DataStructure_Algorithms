def longest_mountain(arr):

    n= len(arr)
    ans=0

    for i in range(1, n-1):

        if (arr[i]> arr[i-1] and arr[i]>arr[i+1]):
            j=i
            

            while (j>0 and arr[j-1]<arr[j]):
                j-=1
                
            k=i
            while(k< n-1 and arr[k]>arr[k+1]):
                k+=1
                

            ans=max(k-j+1,ans)

    return ans    

