from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2)<len(s1):
            return False
        
        left=0

        countS1, countS2= defaultdict(int), defaultdict(int)

        
        for i  in range(len(s1)):

            countS2[s2[i]]+=1
            countS1[s1[i]]+=1

        if countS1 == countS2:
            return True


        for right in range(len(s1), len(s2)) :

            countS2[s2[right]]+=1

            countS2[s2[left]]-=1

            if countS2[s2[left]]==0:
                countS2.pop(s2[left])

            left+=1

            if countS1== countS2:
                return True       

        return False    

        
