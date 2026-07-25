import heapq
from typing import List

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:

        pairs= [(sp,ef) for sp, ef in zip(speed,efficiency)]

        pairs.sort(key= lambda i : i[1] ,reverse=True)

        min_heap= []

        res=0

        emp_speed=0

        for sp, ef in pairs:

            emp_speed += sp

            heapq.heappush(min_heap,sp)

            if len(min_heap) > k:
                sp=-heapq.heappop(min_heap)
                emp_speed-=sp

            
            res= max(
                    res,
                    emp_speed * ef
                )
        return res % (10 ** 9 + 7)


        