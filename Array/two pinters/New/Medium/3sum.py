from typing import List

def threeSum(self, nums:List[int])-> list[List[int]]:
    res=[]
    nums.sort()

    for i, a in enumerate(nums):

        if i>0 and a==nums[i-1]:
            continue

        l,r= i+1, len(nums)-1

        while l<r:
            threeeSum= a+ nums[l]+nums[r]

            if threeeSum>0:
                r-=1

            elif threeeSum<0:
                l+=1

            else:
                res.append([a,nums[l],nums[r]])
                l+=1
                r-=1

                while l< r and nums[l] == nums[l-1]:
                    l+=1

                while l< r and nums[r] == nums[r+1]:
                    r-=1    

    return res                        

