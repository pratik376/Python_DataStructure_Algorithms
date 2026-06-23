def searchInsertion(arr, target):

    l,r =0 , len(arr)-1

    while l<=r:

        mid= (l+r)//2

        if arr[mid]== target:
            return mid
        
        elif arr[mid]> target:
            r=mid-1
        else:
            l=mid+1

    return l


arr=[1,3,5,6]
k=2
print(searchInsertion(arr,k))

                
