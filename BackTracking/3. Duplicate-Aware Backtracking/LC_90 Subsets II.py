class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        res=[]


        def dfs(start, path):


            for i in range(start, len(nums)):

                res.append(path.copy())

                if i > start and nums[i]==nums[i-1]:

                    continue

                path.append(nums[i])
                dfs(i+1, path)
                path.pop()

        dfs(0,[])
        return res

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        res=[]


        def dfs(start, path):

            if start >= len(nums):
                res.append(path[::])
                return

            path.append(nums[start])
            dfs(start+1, path)
            path.pop()

            while start +1 < len(nums) and nums[start] == nums[start+1]:
                start+=1

            dfs(start+1,path) 

        dfs(0,[])
        return res




