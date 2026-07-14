from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        MOD= 10 ** 9+ 7
        subarra_sum=[]

        for i in  range(n):

            curr_sum=0

            for j in range(n):

                curr_sum = (curr_sum + nums[j]) % MOD
                subarra_sum.append(curr_sum)
        
        subarra_sum.sort()

        res=0

        for i in range(left-1, right):
            res= (res + subarra_sum[i])% MOD
        return res
        