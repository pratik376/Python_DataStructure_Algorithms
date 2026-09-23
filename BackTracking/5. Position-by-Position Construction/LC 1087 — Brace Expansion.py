from typing import List


class Solution:
    def expand(self, s: str) -> List[str]:
        groups = []
        res=[]

        i = 0

        while i < len(s):

            if s[i] == "{":
                group = ""
                i += 1
                while s[i] != "}":

                    if s[i] != ",":
                        group += s[i]
                    i += 1
                groups.append(group)
            else:
                groups.append(s[i])
            i += 1
        groups = ["".join(sorted(group)) for group in groups]


        def dfs(position, path):

            if len(path)==len(groups):

                res.append(path[:])
                return

            for ch in groups[position]:

                path.append(ch)

                dfs(position+1, path)
                path.pop()

        dfs(0,[])

        return res

    
