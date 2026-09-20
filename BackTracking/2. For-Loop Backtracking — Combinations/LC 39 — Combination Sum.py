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


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        res=[]

        candidates.sort()


        def combination(start, comb, current_sum):

            
            if current_sum==target:
                res.append(comb.copy())
                return

            for i in range(start, len(candidates)):

                if current_sum + candidates[i] > target:
                    break

                comb.append(candidates[i])
                combination(i, comb, current_sum+ candidates[i])
                comb.pop()

        combination(0,[],0)

        return res

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        res=[]

        def combination(start, comb, current_sum):

            
            if current_sum==target:
                res.append(comb.copy())
                return

            if start >= len(candidates) or current_sum > target:
                return

            
            comb.append(candidates[start])
            combination(start, comb, current_sum + candidates[start])

            comb.pop()
            combination(start +1 , comb, current_sum) 
        combination(0,[],0)

        return res