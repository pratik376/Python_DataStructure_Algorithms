from typing import DefaultDict
def contains_dup(arr,k):

    freq= DefaultDict(int)
    i=0

    for j in range(k):
        freq[arr[j]]+=1

    for r in range(k,len(arr)):

        freq[arr[r]]+=1

        if freq[arr[r]]==2 and r-i <=k:
            return "True"
        else:
            freq[arr[i]]-=1
            i+=1

    return "False"        


def contains_duplicates(nums,k):

    window=set()

    for i, num in enumerate(nums):

        if num in window:
            return True
        
        window.add(num)

        if len(window)>k:
            window.remove(nums[i-k])

    return False        

        
