class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:

        target= sum(nums) // k


        if sum(nums) % k !=0:
            return False


        nums.sort(reverse=True)

        buckets= [0] * k

        def dfs(start):

            if start == len(nums):
                return True

            for j in range(k):

                if nums[start] + buckets[j] <= target:

                    buckets[j] += nums[start]

                    if dfs(start+1):
                        return True

                    buckets[j] -= nums[start]

            return False

        return dfs(0)

