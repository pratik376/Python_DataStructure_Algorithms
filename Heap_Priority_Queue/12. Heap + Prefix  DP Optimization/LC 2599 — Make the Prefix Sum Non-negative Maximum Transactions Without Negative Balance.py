from typing import List
import heapq


class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:

        prefix=0
        moves=0
        min_heap=[]

        for num in nums:
            prefix += num

            if num < 0:
                heapq.heappush(min_heap,num)

            while min_heap and prefix <0:

                worst= heapq.heappop(min_heap)
                prefix -= worst
                moves+=1

        return moves

            
