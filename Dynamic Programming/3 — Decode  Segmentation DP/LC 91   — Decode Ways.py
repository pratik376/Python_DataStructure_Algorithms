class Solution:
    def numDecodings(self, s: str) -> int:

        count=0



        def dfs(start):
            nonlocal count

            if start == len(s):
                count +=1
                return


        


            for end in range(start+1, len(s)+1):

                pices= s[start:end]

                if len(pices) >2:
                    break

                if int(pices[0])==0:
                    continue

                if int(pices) > 26 or int(pices) <1 :
                    continue

                dfs(end)

        dfs(0)
        return count



class Solution:
    def numDecodings(self, s: str) -> int:

        count=0
        memo={}

        def dfs(start):
            nonlocal count

            if start == len(s):
              
                return 1

            if start in memo:
                return memo[start]

            ways=0
            
            for end in range(start+1, len(s)+1):

                pices= s[start:end]

                if len(pices) >2:
                    break

                if int(pices[0])==0:
                    continue # or break

                if int(pices) > 26 or int(pices) <1 :
                    break

                ways+=dfs(end)

            memo[start]= ways
            return ways

        dfs(0)
        return count
        


        

