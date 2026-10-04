from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        count=Counter(nums)

        nums= sorted(list(set(nums)))

        earn1, earn2= 0,0 

        for i in range(len(nums)):

            curr_earn= nums[i] * count[nums[i]]

            