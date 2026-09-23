class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        n= len(digits)
        res=[]
        digitToChar = { "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "qprs",
                "8": "tuv",
                "9": "wxyz" }

        def dfs(pos, path):

            if len(path)==n:

                res.append("".join(path))
                return
            
            for c in  digitToChar[digits[pos]]:
                path.append(c)
                dfs(pos+1,path)
                path.pop()

        if digits:
            dfs(0,[])

        return res
        