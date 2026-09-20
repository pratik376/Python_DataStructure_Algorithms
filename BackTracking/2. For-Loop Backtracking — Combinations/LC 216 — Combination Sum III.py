class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:


        res=[]

        def dfs(start, currentSum, comb):

            if len(comb)>k:
                return
            if currentSum==n and len(comb)==k:
                res.append(comb.copy())
                return

            for i in range(start, 10):

                comb.append(i)
                dfs(i+1, currentSum +i, comb)
                comb.pop()

        dfs(1,0,[])
        return res

class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:

        res=[]

        def dfs(start, currentSum, comb):

            if currentSum > n or len(comb)>k or start > 9:
                return

            if currentSum==n and len(comb)==k:
                res.append(comb.copy())

            # include
            comb.append(start)
            dfs(start+1,currentSum+ start, comb)

            # exclude
            comb.pop()
            dfs(start+1, currentSum,comb)

        dfs(1,0, [])
        return res


         
        


            


            

        