from typing import List
import heapq

# always push opposite to what ever you have sorted
# A better rule to remember

# When you see a greedy + heap problem, ask yourself:

# "What value am I fixing by sorting?"

# Then ask:
# "What remaining value do I need to optimize?"
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


        