class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:

        answer=[]




        def dfs(start, path):


            if len(path)==4 and start==len(s):

                answer.append( ".".join(path.copy()))
                return

            if len(path)>4:
                return

            for end in range(start+1, len(s)+1):

                pices= s[start:end]

                if len(pices) > 0 and pices[0]==0:
                    continue
    
                path.append(pices)

                dfs(end,path)
                path.pop()

        dfs(0,[])
        return answer

                


