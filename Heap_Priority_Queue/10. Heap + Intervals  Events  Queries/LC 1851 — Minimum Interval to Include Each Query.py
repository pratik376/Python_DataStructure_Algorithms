from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort()

        sorted_query = [(val,index) for index, val in enumerate(queries)]

        sorted_query.sort()
        min_heap=[] # (end_time, size_interval)

        answer= [-1] * len(queries)
        i=0


        for val, index in sorted_query:

            while i < len(intervals) and intervals[i][0]<=val:
                heapq.heappush(min_heap, (intervals[i][1],intervals[i][1] - intervals[i][0] +1 ))
                i+=1
            

        
        