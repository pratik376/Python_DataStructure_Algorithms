import heapq
from typing import List
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:

        
        flowers.sort()

        sorted_people =  sorted((time,idx) for idx, time in enumerate(people))

        answer= [] 
        ending_time_heap=[]
        answer=[0] * len(people)

        i=0


        for time,idx in sorted_people:

            while i < len(flowers) and flowers[i][0]<= time:

                heapq.heappush(ending_time_heap, flowers[i][1])
                i+=1

            while ending_time_heap and ending_time_heap[0] < time:
                heapq.heappop(ending_time_heap)

            answer[idx]= len(ending_time_heap)

        return answer 








        