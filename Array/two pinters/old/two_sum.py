nums=[3,2,4]


hashmap={}
def twoSum(nums,target):

    for i, number in enumerate(nums):

        if target-number in hashmap:
            return [hashmap[target-number],i]
        hashmap[number]=i




        

