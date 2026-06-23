


def sqareSortedArray(nums):
    
    n=len(nums)
    left,right=0, n-1
    result=[0]*n

    pos=n-1

    while left<=right:
        if abs(nums[left])> abs(nums[right]):
            result[pos]=nums[left] **2
            ieft+=1
        else:
            result[pos]=nums[right] **2
            right-=1

        pos-=1

    return result        

