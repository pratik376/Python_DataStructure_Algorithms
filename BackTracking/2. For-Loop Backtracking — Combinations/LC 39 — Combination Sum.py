class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        res=[]


        def combination(start, comb, current_sum):

            if current_sum>target:
                return
            
            if current_sum==target:
                res.append(comb.copy())
                return

            for i in range(start, len(candidates)):

                comb.append(candidates[i])
                combination(i, comb, current_sum+ candidates[i])
                comb.pop()

        combination(0,[],0)

        return res