class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        res=[]

        def dfs(position, path):

            if len(path)== n:
                res.append("".join(path))
                return


            for c in "abc":
                
                path.append(c)

                if position> 0 and path[position]==path[position-1]:
                    path.pop()
                    continue
                dfs(position+1, path)
                path.pop()

        dfs(0,[])

        if k > len(res):
            return ""

        return res[k-1]
