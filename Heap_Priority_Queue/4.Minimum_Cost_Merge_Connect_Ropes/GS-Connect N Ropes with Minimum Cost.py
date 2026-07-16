from typing import List
import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:

        cost=0
        heapq.heapify(sticks)

        while len(sticks)> 1:

            s1= heapq.heappop(sticks)
            s2=heapq.heappop(sticks)

            s3= s1+s2

            cost+=s3

            heapq.heappush(sticks,s3)
        return cost

        