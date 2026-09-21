class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:


        candidates.sort()
        res=[]

        def dfs (i, current_sum, path):


            if current_sum==target:
                res.append(path.copy())
                return

            if current_sum > target:
                return

            for j in range(i, len(candidates)):

                if j > i and candidates[j]==candidates[j-1]:
                    continue

                path.append(candidates[j])
                dfs(j+1, current_sum+ candidates[j],path)
                path.pop()

        dfs(0,0,[])
        return res

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:

        candidates.sort()
        res=[]

        def dfs (i, current_sum, path):

            if i >= len(candidates):
                return

            if current_sum==target:
                res.append(path.copy())
                return

            path.append(candidates[i])
            dfs(i+1, current_sum + candidates[i], path)
            path.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
                continue

            dfs(i+1, current_sum, path)

        dfs(0,0,[])
        return res



