# import heapq

# class Solution:
#     def sortArray(self, nums: list[int]) -> list[int]:

#         answer=[]

#         heapq.heapify(nums)

#         while len(nums)> 0:
#             answer.append(heapq.heappop(nums))
        
#         return answer


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        def heapify(n, i):
            while True:
                largest = i
                left = 2 * i + 1
                right = 2 * i + 2

                if left < n and nums[left] > nums[largest]:
                    largest = left

                if right < n and nums[right] > nums[largest]:
                    largest = right

                if largest == i:
                    break

                nums[i], nums[largest] = nums[largest], nums[i]
                i = largest

        n = len(nums)

        # Step 1: Build max heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        # Step 2: Move max element to the end
        for end in range(n - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            heapify(end, 0)

        return nums