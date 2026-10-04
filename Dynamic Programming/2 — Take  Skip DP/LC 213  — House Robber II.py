class Solution:
    def rob(self, nums: list[int]) -> int:

        rob1, rob2= 0,0  # rob1 max previous two , rob2 last

        for i in range(len(nums)-1):

            temp= max(nums[i] +rob1 , rob2)
            rob1=
            rob2= temp


        
        