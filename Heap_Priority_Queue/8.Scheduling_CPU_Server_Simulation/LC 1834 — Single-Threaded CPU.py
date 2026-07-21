from typing import List
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        

        for i,t in enumerate(tasks):
            t.append(i)
        
        tasks.sort(key= lambda t: t[0])

        res, min_heap= [], []
        i, time= 0, tasks[0][0]

        while min_heap or i < len(tasks):

            while i < len(tasks) and time >=

