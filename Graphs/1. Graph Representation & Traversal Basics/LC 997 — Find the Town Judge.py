from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        juge= 0 
        count=0
        visited= set()

        for personA, personB in trust:

           if [personA,personB] not in visited:
            count+=1
            visited.add([personA,personB])

            if juge ==0:
                juge= personB

            elif (juge != personB):
                return -1

        if count < n-1:
            return -1

        return juge

