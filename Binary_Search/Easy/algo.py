def binary(arr,n,key):

    l=0
    r=n-1

    while (l<=r):
        mid= (l+r) //2

        if key== arr[mid]:
            return mid
        elif key < arr[mid]:
            r=mid-1
        else:
            l=mid+1

    return -1            

