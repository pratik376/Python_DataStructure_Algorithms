from typing import List
import heapq

class Solution:
    def minHeapToMaxHeap(self, heap: List[int]) -> List[int]:

        heap = [-val for val in heap]
        heapq.heapify(heap)

        heap = [-val for val in heap]

        return heap


