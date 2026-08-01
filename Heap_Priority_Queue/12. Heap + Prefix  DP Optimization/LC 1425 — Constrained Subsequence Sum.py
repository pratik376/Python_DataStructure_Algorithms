from typing import List
import heapq


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        res=nums[0]

        heap_max=[(-nums[0],0)] # max_sum, index

        for i in range(1, len(nums)):

            while i - heap_max[0][1] > k:
                heapq.heappop(heap_max)

            curr_max= max(nums[i], nums[i]-heap_max[0][0])
            res= max(res,curr_max)

            heapq.heappush(heap_max, (-curr_max,i))

        return res





        
        