class Solution:
    def maxLength(self, arr: list[str]) -> int:

        answer=0

        def calculate_uniq(current,newstring):

            combined= current + newstring

            return len(combined) == len(set(combined))

        def dfs(i, curr_String):
            nonlocal answer

            if i >= len(arr):
                answer=max(answer,len(curr_String))
                return

            if calculate_uniq(curr_String,arr[i]):  # calculate whether there are unique characters if yes then proced else not proceed
                dfs(i+1, len(arr[i])+ len(arr[i+1]))

            dfs(i+1,curr_String) # without adding

        dfs(0,"")
        return answer

        




            

        