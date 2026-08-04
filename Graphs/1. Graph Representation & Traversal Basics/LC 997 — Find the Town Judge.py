from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        juge= 0 

        for personA, personB in trust:

            if juge ==0:
                personB= juge

            elif (juge != personB):
                return -1

        return juge

