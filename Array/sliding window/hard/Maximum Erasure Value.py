from collections import defaultdict

def erase_value(arr):

    window_sum=0
    max_sum=float('-inf') # or 0
    fre= defaultdict(int)
    left= 0


    for right in range(len(arr)):

        fre[arr[right]]+=1

        window_sum+=arr[right]

        while fre[arr[right]]==2 :
            fre[arr[left]]-=1

            if not fre[arr[left]]:
                fre.pop(arr[left])

            window_sum-=arr[left]
            left+=1

        max_sum=max(max_sum,window_sum)        
    
    return max_sum
        




