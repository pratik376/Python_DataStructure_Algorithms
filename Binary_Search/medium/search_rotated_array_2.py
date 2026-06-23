def search(arr,target):
    l,r = 0, len(arr)-1

    while l<=r:

        mid= (l+r) //2

        if arr[mid]== target:
            return mid
        
        if arr[l] < arr[mid]: # left portion 
            if arr[l]<=target<arr[mid]:
                r=mid-1
            else:
                l=mid+1

        elif arr[mid]< arr[r]: # right portion

            if arr[mid] < target <= arr[r]:
                l=mid+1
            else:
                r=mid-1
        else:
            l+=1                       
    return False
