from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        

        for i,t in enumerate(tasks):
            t.append(i)
        
        tasks.sort(key= lambda t: t[0])
        