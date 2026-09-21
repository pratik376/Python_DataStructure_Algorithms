from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:

        res=[]

        def dfs(i, path, factor):

            if factor > n:
                return

            if factor==n and len(path) >=2:
                res.append(path.copy())
                return

            for j in range(i, n+1):

                if j * factor > n:
                    break

                if n % (j * factor) !=0:
                    continue
                 
                path.append(j)
                dfs(j, path, factor * j)
                path.pop()

        dfs(2,[],1)
        return res


            

            


        