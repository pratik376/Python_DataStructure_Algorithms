from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort()

        sorted_query = [(val,index) for index, val in enumerate(queries)]
        
        