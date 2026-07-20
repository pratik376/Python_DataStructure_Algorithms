from typing import List
from collections import Counter,deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count= Counter(tasks)
        max_heap= [-val for val in count.values()]
        heapq.heapify(max_heap)
        q=deque()
        time=0
        
        while max_heap or q:
            time+=1

            if max_heap:

                freq= 1+heapq.heappop(max_heap) # decreasing frequncy

                if freq:
                    q.append([freq,time+n])
            
            if q and q[0][1]== time:
                heapq.heappush(q.popleft()[0])
        
        return time
        