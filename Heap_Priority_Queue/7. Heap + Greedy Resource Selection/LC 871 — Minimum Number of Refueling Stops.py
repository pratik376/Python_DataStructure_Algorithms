import heapq
from typing import List
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:

        Maxheap=[]

        stations.sort() 

        current_mile=0

        for position, fuel in stations:

            startFuel-=position
            startFuel += fuel
            current_mile+= position
            heapq.heappush(heap,fuel)
            


            if current_mile >= target:
                return len(heap)

            if current_mile <


        