from collections import defaultdict

class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:


        frq = defaultdict(int)

        for word in letters:

            frq[word]+=1

        
        