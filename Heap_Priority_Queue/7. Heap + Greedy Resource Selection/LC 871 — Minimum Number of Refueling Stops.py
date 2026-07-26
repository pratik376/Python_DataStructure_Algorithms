import heapq
from typing import List
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:

       stations.append([target,0])

       heap=[]
       stops=0
       fuel=startFuel
       prev=0


       for position, station_fuel in stations:

           fuel-= (position-prev)
           heapq.heappush(heap, - station_fuel)

           while heap and fuel <0:
               fuel += - heapq.heappop(heap)
               stops+=1

           if fuel < 0:
               return -1
           prev=position

       return stops
           
           
           


        