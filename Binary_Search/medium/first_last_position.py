def searchRange(arr, target):

    



    def binaraySearch(arr,target, leftBias):

        l,r= 0, len(arr)-1
        i=-1
        while l<=r:

            mid= (l+r)//2

            if target > arr[mid]:
                l=mid+1
            elif target < arr[mid]:
                r=mid-1

            else:
                i=mid

                if leftBias:
                    r=mid-1
                else:
                    l=mid+1

        return i                
    
    left= binaraySearch(arr,target,True)
    right= binaraySearch(arr,target,False)
    return [left, right]
