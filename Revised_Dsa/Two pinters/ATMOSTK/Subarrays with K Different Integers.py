from typing import List
from collections import defaultdict

def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

    def atMost(x):

        if x< 0:
            return 0
        
        count= defaultdict(int)
        answer=0
        left=0
        for right in range(len(nums)):

            count[nums[right]]+=1

            while len(count)> x:
                count[nums[left]]-=1
                if count[nums[left]]==0:
                    del count[nums[left]]
                left+=1

            answer += (right-left+1) 
        return answer       
    return atMost(k)-atMost(k-1)       