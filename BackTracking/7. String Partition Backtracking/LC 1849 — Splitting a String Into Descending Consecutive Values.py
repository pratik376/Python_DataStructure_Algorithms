class Solution:
    def splitString(self, s: str) -> bool:
        
        res=[]

        
                

        def dfs (start, path):


            if len(res)>=2:
                return True

            if start==len(s):
                res.append(path.copy())
                return


            for end in range(start+1, len(s)+1):


                piece=s[start:end]

                if int(path)-int(piece)==1:

                    path.add(piece)

                    if dfs(end,path):
                        return True
                    path.pop()
            return False

        return dfs(0,[])


