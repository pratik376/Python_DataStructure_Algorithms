class Solution:
    def splitString(self, s: str) -> bool:
        
        res=[]

        
                

        def dfs (start, path):

            if start==len(s):
             
                return len(path) >=2


            for end in range(start+1, len(s)+1):


                piece=s[start:end]

                if not path or path and int(path[-1])-int(piece)==1:

                    path.append(piece)

                    if dfs(end,path):
                        return True
                    path.pop()
            return False

        return dfs(0,[])


