class Solution:
    def partition(self, s: str) -> list[list[str]]:

        answer=[]
        
        def dfs(start, path):

            if start== len(s):
                answer.append(path.copy())

            for end  in range(start+1, len(s)+1):

                pieces=s[start:end]

                if pieces[0]==pieces[-1]:

                    path.append(pieces)
                    dfs(end)
                    path.pop()

        return answer

        

        

            