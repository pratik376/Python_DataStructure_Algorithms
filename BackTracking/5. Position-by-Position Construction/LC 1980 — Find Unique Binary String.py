class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:


        if not nums:
            return ""

        num_set= set(nums)
        n= len(nums[0])

        answer=[]


        def dfs(position, path):

            if len(path)== n and "".join(path) not in num_set:
                answer.append("".join(path))
                return

            for c in "01":

                if answer:
                    return

                path.append(c)
                dfs(position+1)
                path.pop()

        dfs(0,[])
        return "".join(answer)

                




