from typing import List
import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        for i in range(times):
            times[i].append(i)

        times.sort(lambda x : x[0])

        availbe_chair=[i for i in range(times)]
        busy_chair=[]

        for time in times:

            arrival, end, position= time

            while busy_chair and arrival>=busy_chair[0][0]:
                end_time, chair_number=heapq.heappop(busy_chair)
                heapq.heappush(availbe_chair,chair_number)

            chair_number= heapq.heappop(availbe_chair)

            if position==targetFriend:
                return 

            heapq.heappush(busy_chair, (end, chair_number))





            


         


        