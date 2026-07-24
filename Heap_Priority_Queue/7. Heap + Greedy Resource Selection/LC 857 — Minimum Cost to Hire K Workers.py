from typing import List
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:

        res= float("inf")
        pairs=[]

        for i in range(len(quality)):
            pairs.append( (wage[i]/quality[i], quality[i]))

        pairs.sort()



        