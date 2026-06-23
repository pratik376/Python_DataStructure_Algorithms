def numSubarraysWithSum(nums, goal):

    def atMost(k):

        if k <0:
            return 0
        
        left=0
        current_sum=0
        res=0

        for right in range(len(nums)):

            current_sum+=nums[right]

            while current_sum > k:
                current_sum-=nums[left]
                left+=1

            res=right-left+1

        return res    

    return atMost(goal) - atMost(goal-1)         

