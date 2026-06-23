def sort_colors(arr):

    l,r=0, len(arr)-1

    i=0

    def swap(i,j):

        tmp=arr[i]
        arr[i]=arr[j]
        arr[j]=tmp

    while i<=r:

        if arr[i]==0:

            swap(l,i)
            i+=1

        elif arr[i]==2:
            swap(i,r)
            r-=1
            i-=1
        i+=1    


            