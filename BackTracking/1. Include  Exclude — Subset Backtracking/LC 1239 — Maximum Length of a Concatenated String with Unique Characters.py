class Solution:
    def maxLength(self, arr: list[str]) -> int:

        answer=0

        def calculate_uniq(s1,s2):
            s1,s2= set(s1),set(s2)

            for ch in s1:

                if ch in s2:
                    return False

            return True


        def dfs(i, uniq_char):
            nonlocal answer

            if i >= len(arr):
                answer=max(answer,uniq_char)
                return

            if calculate_uniq(arr[i],arr[i+1]):  # calculate whether there are unique characters if yes then proced else not proceed
                dfs(i+1, len(arr[i])+ len(arr[i+1]))

            dfs(i+1, uniq_char) # without adding

        




            

        