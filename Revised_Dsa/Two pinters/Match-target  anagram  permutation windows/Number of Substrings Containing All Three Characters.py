from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        left=0
        freq=defaultdict(int)
        result=0
        

        for right in range(len(s)):

            freq[s[right]]+=1

            while len(freq)==3:
                result+= (len(s)-right)
                freq[s[left]]-=1

                if freq[s[left]]==0:
                    freq.pop(s[left])

                left+=1
             
        return result                
