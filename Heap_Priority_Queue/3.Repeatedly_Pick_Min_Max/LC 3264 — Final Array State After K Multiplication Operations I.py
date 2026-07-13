from typing import List
import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        heapq.heapify(nums) # O(n)

        for _ in range(k):  # O(k)

            element=heapq.heappop(nums) # log(n)

            heapq.heappush(nums, multiplier * element) # log(n)
        
        return nums
    
    # space complexity O(1)
    # time complexity O(n + 2k log(n) ) ==> 0(n+ klongn)


        