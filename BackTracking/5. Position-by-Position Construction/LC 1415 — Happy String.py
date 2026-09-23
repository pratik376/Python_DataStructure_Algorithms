class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        res=[]

        def dfs(position, path):

            if len(path)== n:
                res.append("".join(path))
                return

            for c in "abc":
                
                # path.append(c)

                # if position> 0 and path[position]==path[position-1]:
                #     path.pop()
                #     continue

                if path and c == path[-1]:
                    continue

                path.append(c)

                dfs(position+1, path)
                path.pop()

        dfs(0,[])

        if k > len(res):
            return ""

        return res[k-1]

# 39 mins
class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        count=0

        def dfs(position, path):
            nonlocal count

            if len(path)== n:

                count+=1

                if count == k:
                    return  "".join(path)

                return

            for c in "abc":
                
                if path and c == path[-1]:
                    continue

                path.append(c)

                answer = dfs(position+1, path)

                if answer:
                    return answer
                
                path.pop()
            return ""

        return dfs(0,[])
       

