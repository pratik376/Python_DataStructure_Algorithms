from typing import List
import heapq

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        MOD= 10 ** 9+ 7
        subarra_sum=[]

        for i in  range(n):

            curr_sum=0

            for j in range(i,n):

                curr_sum = (curr_sum + nums[j]) % MOD
                subarra_sum.append(curr_sum)
        
        subarra_sum.sort()

        res=0

        for i in range(left-1, right):
            res= (res + subarra_sum[i])% MOD
        return res
    
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        MOD= 10 ** 9+ 7
        heap= [(n,i) for i,n in enumerate(nums)]
        heapq.heapify(heap)
        res=0
        

        for i in range(right):
            num, index= heapq.heappop(heap)

            if i >= left-1:
                res= (res + num) % MOD
            
            if index + 1 < n:
                next_pair= (nums+ nums[index+1], index+1)
                heapq.heappush(heap,next_pair)

        return res
        
        