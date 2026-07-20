from typing import List
from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count= Counter(tasks)
        max_heap= [-val for val in count.values()]
        
        