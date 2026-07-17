from typing import List
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        heap=[]
        answer=0

        for i in range(len(matrix)):

            heapq.heappush(heap, (matrix[i][0], i, 0))  # value, array number, index

        while  k > 0:

            value, array_number, index= heapq.heappop(heap)

            answer=value

            if index+1 < len(matrix[array_number]):
                heapq.heappush(heap, (matrix[array_number][index+1], array_number,index+1))

            k-=1
        
        return answer
        
        


        