
def sortedColor(arr):

    l,mid,r=0,0,len(arr)-1

    

    while(mid<=r):
        
        if arr[mid]==0:
            arr[mid],arr[l]=arr[l],arr[mid]
            l+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
            
        
        else:
            arr[mid],arr[r]=arr[r],arr[mid]
            r-=1

    return arr             






