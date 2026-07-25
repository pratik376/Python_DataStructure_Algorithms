from typing import List
import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:

        courses.sort( key= lambda x : x[1])

        maxHeap=[]

        totalDays=0

        for duration, lastDay in courses:

            totalDays+=duration

            heapq.heappush(maxHeap, -duration)

            if totalDays > lastDay:
                maxday= -heapq.heappop(maxHeap)
                totalDays-=maxday

        return len(maxHeap)


        