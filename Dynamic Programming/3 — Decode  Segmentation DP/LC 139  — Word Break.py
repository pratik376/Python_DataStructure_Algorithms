class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:

        words= set(wordDict)

        memo={}

        def dfs(start):
            nonlocal memo

            if start in memo:
                return memo[start]
            
            if start == len(s):
                return True
                
            for end in range(start+1, len(s)+1):

                pices= s[start:end]

                if pices not in words:
                    continue

                if dfs(end):
                    memo[start]=True
                    return True

            memo[start]=False
            return False
        return dfs(0,"")
    



        





