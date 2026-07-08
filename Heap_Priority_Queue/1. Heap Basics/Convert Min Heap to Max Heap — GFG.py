from typing import List
import heapq

class solution:
    def minHeapToMaxHeap(heap: List[int]) -> List[int]:

        heap = [-val for val in heap]
        