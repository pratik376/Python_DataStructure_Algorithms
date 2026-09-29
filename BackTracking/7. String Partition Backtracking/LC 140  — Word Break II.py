class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:


        res=[]
        words= set(wordDict)


        def dfs(start, path):

            if start== len(str):

                res.append(" ".join(path))

            for end in range(start+1, len(s)+1):

                piece= s[start:end]

                if piece in words:

                    path.append(piece)
                    dfs(end, path)
                    path.pop()

        dfs(0,[])
        return res
        