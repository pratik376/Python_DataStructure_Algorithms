from typing import List
import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        k= len(nums)
        heap=[]

        left=right= nums[0][0]

        for i in range(k):

            l= nums[i]

            left= min(left, l[0])
            right= max(right, l[0])
            heapq.heappush(heap, (l[0], i, 0)) # (element, index, element_index)
        
        res=[left, right]

        while True:

            n, i ,idx= heapq.heappop(heap)

            idx+=1

            if idx == len(nums[i]):
                break

            next_val= nums[i][idx]

            heapq.heappush(heap, (next_val,i,idx))

            right= max(right, next_val)
            left= heap[0][0]

            if right - left < res[1] - res[0]:
                res=[left, right]
        return res

