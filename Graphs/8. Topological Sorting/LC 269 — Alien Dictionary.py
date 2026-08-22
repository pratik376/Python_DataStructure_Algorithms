from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:

        adj= {c: set() for word in words for c in word}

        for i in range(len(words)-1):

            w1,w2 = words[i],words[i+1]

            
        