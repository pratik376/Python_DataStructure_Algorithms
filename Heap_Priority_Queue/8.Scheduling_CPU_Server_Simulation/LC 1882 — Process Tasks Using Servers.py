from typing import List


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        
        # two min heaps, one for available server and one for unavailable
        # available =(weight, index)
        # unavailable = (timeserveBecomesAvailable, weight, index)
        