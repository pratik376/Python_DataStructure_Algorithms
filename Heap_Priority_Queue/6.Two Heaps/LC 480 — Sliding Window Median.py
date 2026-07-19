from typing import List
import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        min_heap = []   # right
        max_heap = []   # left (store negatives)

        delayed = defaultdict(int)

        answer = []

        max_size = 0
        min_size = 0

        def prune_max():
            while max_heap:
                val = -max_heap[0]
                if delayed[val]:
                    delayed[val] -= 1
                    heapq.heappop(max_heap)
                else:
                    break

        def prune_min():
            while min_heap:
                val = min_heap[0]
                if delayed[val]:
                    delayed[val] -= 1
                    heapq.heappop(min_heap)
                else:
                    break

        def balance():
            nonlocal max_size, min_size
            prune_min()
            prune_max()

            if max_size > min_size + 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
                max_size -= 1
                min_size += 1
                
            elif min_size > max_size:
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
                min_size -= 1
                max_size += 1
                

        for i in range(len(nums)):

            # -------- insert --------
            if not max_heap or nums[i] <= -max_heap[0]:
                heapq.heappush(max_heap, -nums[i])
                max_size += 1
            else:
                heapq.heappush(min_heap, nums[i])
                min_size += 1

            balance()

            # -------- remove outgoing --------
            if i >= k:

                out = nums[i - k]
                delayed[out] += 1

                if out <= -max_heap[0]:
                    max_size -= 1
                    if out == -max_heap[0]:
                        prune_max()
                else:
                    min_size -= 1
                    if min_heap and out == min_heap[0]:
                        prune_min()

                balance()

            # -------- median --------
            if i >= k - 1:

                prune_max()
                prune_min()

                if k % 2 == 1:
                    answer.append(float(-max_heap[0]))
                else:
                    answer.append((-max_heap[0] + min_heap[0]) / 2)

        return answer