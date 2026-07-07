from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums

        self.nums=[-val for val in self.nums]
        heapq.heapify(self.nums)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums,-val)

        return -self.nums[self.k-1]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)