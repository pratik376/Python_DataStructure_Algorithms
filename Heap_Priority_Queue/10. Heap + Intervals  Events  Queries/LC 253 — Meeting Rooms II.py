from typing import List
import heapq

class Interval:
    def __init__(self,start,end):
        self.start= start
        self.end= end

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:


        start= sorted([i.start for i in intervals])
        end= sorted([i.end for i in intervals])
        res ,count = 0,0 

        s,e = 0,0 

        while s < len(intervals):

            if start[s] < end[e]:
                s+=1
                count+=1
            else:
                e+=1
                count-=1

            res = max(res,count)

        return res


            
         
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0

        intervals.sort()
        end_heap=[]
        rooms=0

        for star, end in intervals:

            while end_heap and end_heap[0] <=star:
                heapq.heappop(end_heap)

            heapq.heappush(end_heap, end)

            rooms= max(rooms, len(end_heap))

        return rooms




