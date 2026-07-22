from typing import List
import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        for i in range(len(times)):
            times[i].append(i)

        times.sort(key=lambda x : x[0])

        availbe_chair=[i for i in range(len(times))]
        busy_chair=[]

        for time in times:

            arrival, end, position= time

            while busy_chair and arrival>=busy_chair[0][0]:
                end_time, chair_number=heapq.heappop(busy_chair)
                heapq.heappush(availbe_chair,chair_number)

            chair_number= heapq.heappop(availbe_chair)

            if position==targetFriend:
                return chair_number

            heapq.heappush(busy_chair, (end, chair_number))





            


         


        