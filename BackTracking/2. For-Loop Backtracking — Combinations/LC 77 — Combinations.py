class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:

        res=[]

        def combination (i, comb):

            if len(comb)==k:
                res.append(comb.copy())
                return


            for j in range(i,n+1):

                comb.append(j)

                combination(j+1, comb)

                comb.pop()

        combination(1,[])

        return res
