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


