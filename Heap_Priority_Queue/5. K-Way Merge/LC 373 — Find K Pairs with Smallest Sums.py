from typing import List
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        heap=[]

        answer=[]

        for i in range(min(len(nums1),k)):
            heapq.heappush(heap, (nums1[i]+nums2[0], i,0))
        
        while heap and k:

            sum, i, j = heapq.heappop(heap)

            answer.append([nums1[i],nums2[j]])

            if j+1 < len(nums2):
                heapq.heappush(heap, (nums1[i]+ nums2[j+1], i, j+1))
            
            k-=1

        return answer


