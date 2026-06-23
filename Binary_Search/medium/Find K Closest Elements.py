def myarr(arr, k ,x):

    l, r= 0 , len(arr)-k

    while l<r:
        mid= (l+r) //2

        if l < r:

            if x-arr[mid] > arr[mid+k]-x:
                l=mid+1
            else:
                r=mid

    return arr[l:l+k]            

print([5,7,8,9,10,13],3,8)