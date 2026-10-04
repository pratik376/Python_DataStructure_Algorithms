class Solution:
    def rob(self, nums: list[int]) -> int:

        rob1, rob2= 0,0  # rob1 max previous two , rob2 last

        for i in range(len(nums)-1):

            temp= max(nums[i] +rob1 , rob2)
            rob1= rob2
            rob2= temp

        answer1= rob2

        rob1, rob2= 0,0

        for i in range(1, len(nums)):

            temp= max(nums[i] + rob1, rob2)
            rob1=rob2
            rob2=temp

        answer2=rob2

        return max(answer1,answer2)



        
        