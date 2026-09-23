from typing import List


class Solution:
    def expand(self, s: str) -> List[str]:

        index=-1
        groups=[]

        i=0

        while i < len(s):

            index+=1

            if s[i]=="{":
                group=""

                i+=1

                while s[i] !="}":

                    if s[i] !=',':
                       group+=(s[i])
                    i+=1

                groups.append(group)

            else:
                groups[index].append(s[i])

            i+=1


        

        