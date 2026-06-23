def pickElement(arr):

    l, r= 0, len(arr)-1

    while l<=r:

        mid= (l+r)//2

        if mid < len(arr)-1  and arr[mid] < arr[mid+1]:
            l=mid+1
        elif mid >0 and arr[mid] < arr [mid-1]:
            r=mid-1
        else:
            return mid