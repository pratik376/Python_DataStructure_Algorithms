class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        res=[]


        def combination(start, comb):

            if sum(comb)==target:
                res.append(comb.target())
                return


            for i in range(start, len(candidates)):

                comb.append(i)
                combination(i, comb)
                comb.pop()

        combination(0,[])

        return res