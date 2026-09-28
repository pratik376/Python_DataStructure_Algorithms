class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        count=0
        used={}

        def dfs(start, path):
            nonlocal count

            if start== len(s):

                if len(path)==len(set(path)):
                    count+=1
                return

            for end in range(start+1 , len(s)+1):

                piece= s[start:end]  # aba -->3  now -> set -> {a,b} -> 2

                if piece not in used:

                    used.add(piece)
                    path.append(piece)
                    dfs(end,path)

                    path.pop()
                    used.remove(piece)

        dfs(0,[])
        return count
        
