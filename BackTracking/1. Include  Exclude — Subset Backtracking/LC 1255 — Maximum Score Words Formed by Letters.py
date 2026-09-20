from collections import defaultdict

class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:


        frq = defaultdict(int)
        answer=0

        for word in letters:

            frq[word]+=1


        def calculate_char(current_String):
            sum=0

            for ch in current_String:
                if frq[ch]==0:
                    return 0
                frq[ch]-=1
                idx = ord(ch) - ord('a')
                sum+= score[idx]

            return sum

        def addingToDict(currentString):
            for ch in currentString:

                frq[ch]+=1


        def dfs(i, string):
            nonlocal answer
            if i>= len(words):
                return


            # add

            can_add= calculate_char(words[i])
            answer+=can_add
            if can_add:

                dfs(i+1, string+ words[i])

                addingToDict(words[i])

            dfs(i+1, string)

        dfs(0,"")
        return answer



            

            

        
        