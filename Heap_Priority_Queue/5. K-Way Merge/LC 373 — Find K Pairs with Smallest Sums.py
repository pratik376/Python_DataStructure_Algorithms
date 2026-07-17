from typing import List
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        heap=[]

        answer=[]

        for i in range(min(len(nums1,nums2))):
            heapq.heappush((nums1[i] + nums2[i], i,i))    

        while k:

            sum, i,j = heapq.heappop(heap)

            answer.append([nums1[i],nums2[j]])

            if nums1[i] < nums2[j] and j + 1 < len(nums2):

                heapq.heappush(heap, (nums1[i] + nums1[j+1], i,j+1))
            
            elif nums2[j] < nums1[i]  and i+ 1 < len(nums1):
                heapq.heappush(heap, (nums1[i] + nums1[j+1], i+1,j))
            
            k-=1
        
        return answer


