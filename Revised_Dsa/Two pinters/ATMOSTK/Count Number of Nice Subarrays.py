from typing import List


def numberOfSubarrays(self, nums: List[int], k: int) -> int:


    def Atmost(k):

        left=0
        answer=0
        count_odd=0

        for right in range(len(nums)):

            if nums[right] %2 !=0:
                count_odd+=1

            while count_odd>k:

                if nums[left] %2 != 0:
                    count_odd-=1
                left+=1
            answer+= (right-left+1)
        return answer
    return Atmost(k)- Atmost(k-1)                    
