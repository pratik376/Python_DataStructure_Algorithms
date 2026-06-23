from typing import List

def numberOfSubarrays(self, nums: List[int], k: int) -> int:

    def atMost(k):
        if k<1:
            return 0
        
        left=0
        count=0
        res=0

        for right in range(len(nums)):

            if nums[right] %2 !=0:
                count+=1

            while count > k:
                if nums[left] % 2 !=0:
                    count-=1
                    
                left+=1

            res+= right-left+1

        return res

    return atMost(k) - atMost(k-1)            

                    
 