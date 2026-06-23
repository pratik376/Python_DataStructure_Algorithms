

from collections import defaultdict


def longestRepeatingCharacter(s,k):

    left=0
    dict=defaultdict(int)
    max_freq=0
    max_length=0


    for right in range(len(s)):

        dict[s[right]]+=1

        max_freq=max(max_freq,dict[s[right]])

        while (right-left +1 ) - max_freq >k:
            dict[s[left]]-=1
            left+=1

        max_length=max(max_length,right-left+1)

    return max_length    





