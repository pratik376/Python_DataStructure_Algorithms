# import heapq

# class Solution:
#     def sortArray(self, nums: list[int]) -> list[int]:

#         answer=[]

#         heapq.heapify(nums)

#         while len(nums)> 0:
#             answer.append(heapq.heappop(nums))
        
#         return answer


import heapq

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        nums= [-val for val in nums]

        heapq.heapify(nums)

        for i in range(len(nums)-1, -1,-1):

            largest=-heapq.heappop(nums)
            nums[i]=largest
        
        return nums
