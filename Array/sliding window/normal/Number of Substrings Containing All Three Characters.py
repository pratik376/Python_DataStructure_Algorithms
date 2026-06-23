from collections import defaultdict

def numbofSubString(str):

    left=0
    result=0
    frequency= defaultdict(int)

    for right in range(len(str)):

        frequency[str[right]]+=1

        while len(frequency)==3:

            result+= len(str)- right

            frequency[str[left]]-=1

            if frequency[str[left]]==0:
                frequency.pop([str[left]])
            left+=1
    return result        



class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        res = 0
        count = [0] * 3   # count[0]=a, count[1]=b, count[2]=c

        for r in range(len(s)):
            count[ord(s[r]) - ord('a')] += 1

            while count[0] and count[1] and count[2]:
                res += len(s) - r
                count[ord(s[l]) - ord('a')] -= 1
                l += 1

        return res