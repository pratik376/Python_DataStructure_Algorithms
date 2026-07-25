from typing import List
import heapq

# always push opposite to what ever you have sorted
# A better rule to remember

# When you see a greedy + heap problem, ask yourself:

# "What value am I fixing by sorting?"

# Then ask:
# "What remaining value do I need to optimize?"

# now how do i know which one should i sort ?

# Use this rule:

# Sort by the value that fixes the boundary of what is currently possible.
# Then use the heap for the value you still want to optimize.

# A simple way to ask it is:

# “At this step, what makes an item available or valid?”

# That is usually the thing to sort by.
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


        