from collections import defaultdict

def longestSubstring(str):


    answer=0
    left=0
    freq=defaultdict(int)


    for right in range(len(str)):

        freq[str[right]]+=1


        while freq[str[right]] >1:

            freq[str[left]]-=1

            if freq[str[left]] ==0:
                del freq[str[left]]

            left+=1
        answer= max(answer, right-left+1)
    return answer            

