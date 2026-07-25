import heapq
from typing import List

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:

        pairs= [(sp,ef) for sp, ef in zip(speed,efficiency)]

        pairs.sort(reverse=True)

        max_heap= []

        res=0

        emp_speed=0

        for sp, ef in pairs:

            emp_speed += sp

            heapq.heappush(max_heap,-sp)

            if len(max_heap) > k:
                sp=-heapq.heappop(max_heap)
                emp_speed-=sp

            
            res= max(
                    res,
                    emp_speed * ef
                )

        return res


        