from typing import List
import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        
        # two min heaps, one for available server and one for unavailable
        # available =(weight, index)
        # unavailable = (timeserveBecomesAvailable, weight, index)

        res= [0] * len(tasks)

        available= [(servers[i],i) for i in range(len(servers))]
        available=heapq.heapify(available)
        unavailable= []
        time=0

        for i in range(len(servers)):
            time= max(i,time)

            if not available:
                time= unavailable[0][0]
            
            while unavailable and time >= unavailable[0][0]:
                timefree, w, index = heapq.heappop(unavailable)
                heapq.heappush(available, (w,index))
            
            w, index = heapq.heappop(available)
fds
            res[i]=index

            heapq.heappush(unavailable, (time+ tasks[i],w,index))
        return res
            

