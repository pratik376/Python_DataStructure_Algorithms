class Solution:
    def numDecodings(self, s: str) -> int:

        count=0



        def dfs(start):

            if start == len(s):
                count +=1
                return


            for end in range(start+1, len(s)+1):

                pices= s[start:end]

                