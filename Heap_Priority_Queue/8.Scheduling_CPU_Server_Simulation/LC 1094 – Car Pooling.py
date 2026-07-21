from typing import List
import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        # solution 1 #O(n)

        passChange =[0] * 1001

        for t in trips:
            numPass,start, end= t

            passChange[start] += numPass
            passChange[end]-= numPass
        
        curr=0

        for i in range(1001):

            curr+= passChange[i]

            if curr > capacity:
                return False
        return True
         

        #solution 2 O(nlogn)

        trips.sort(key= lambda t: t[1])
        minHeap=[]
        currPass=0

        for t in trips:
            numPass, start, end = t

            while minHeap and start >=minHeap[0][0]:
                currPass-=heapq.heappop(minHeap)

            currPass+= numPass

            if currPass> capacity:
                return False

            heapq.heappush(minHeap, [end,numPass])
        return True



    
    

  
        