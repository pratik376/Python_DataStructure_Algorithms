from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs= [(n1,n2) for n1,n2 in zip(nums1, nums2)]
        pairs= sorted(pairs, key= lambda x : x[1], reverse=True)
        