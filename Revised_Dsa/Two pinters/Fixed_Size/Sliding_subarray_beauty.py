from collections import deque

class Solution:
    def getSubarrayBeauty(self, nums, k, x):
        freq = [0] * 101   # map value v -> v + 50
        ans = []

        # first window
        for i in range(k):
            freq[nums[i] + 50] += 1

        def find_xth_smallest_negative():
            count = 0

            # only check negative numbers: -50 to -1
            for v in range(0, 50):
                count += freq[v]

                if count >= x:
                    return v - 50

            return 0

        ans.append(find_xth_smallest_negative())

        left = 0

        for right in range(k, len(nums)):
            freq[nums[right] + 50] += 1
            freq[nums[left] + 50] -= 1
            left += 1

            ans.append(find_xth_smallest_negative())

        return ans