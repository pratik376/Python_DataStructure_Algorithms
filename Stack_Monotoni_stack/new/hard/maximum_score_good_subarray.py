from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        l = r = k
        res = nums[k]
        cur_min = nums[k]

        while l > 0 or r < len(nums) - 1:
            left = nums[l - 1] if l > 0 else 0
            right = nums[r + 1] if r < len(nums) - 1 else 0

            if left > right:
                l -= 1
                cur_min = min(cur_min, left)
            else:
                r += 1
                cur_min = min(cur_min, right)

            res = max(res, cur_min * (r - l + 1))

        return res


from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums = [0] + nums + [0]  # add sentinel to simplify stack
        k += 1  # shift index due to sentinel
        stack = []
        res = 0
        
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                height_index = stack.pop()
                height = nums[height_index]
                left = stack[-1] if stack else -1
                right = i
                # Check if the subarray contains k
                if left < k < right:
                    width = right - left - 1
                    res = max(res, height * width)
            stack.append(i)
        
        return res