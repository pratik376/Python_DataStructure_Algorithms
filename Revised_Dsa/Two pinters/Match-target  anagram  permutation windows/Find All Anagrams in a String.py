from typing import List
from collections import defaultdict


# if dynamic sliding window not work try fixed sized window
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        countS, countP = defaultdict(int), defaultdict(int)
        result=[]

        if len(s) < len(p):
            return []
        

        for i in range(len(p)):
            countP[p[i]]+=1
            countS[s[i]]+=1

        if countP== countS:
            result.append(0)
            
        left=0

        for r in range(len(p), len(s)):

            countS[s[r]]+=1

            countS[s[left]]-=1

            if countS[s[left]]==0:
                countS.pop(s[left])

            left+=1    

            if countP==countS:
                result.append(left)    

        