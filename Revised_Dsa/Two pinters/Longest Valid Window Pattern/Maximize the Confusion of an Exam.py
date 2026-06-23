from collections import defaultdict
def maximizeConfusing(string, k):

    left=0
    max_frq=0
    freq=defaultdict(int)
    answer=0


    for right in range(len(string)):

        freq[string[right]]+=1

        max_frq= max(max_frq, freq[string[right]])

        while (right-left+1) - max_frq >k:

            freq[string[left]]-=1

            left+=1
        answer= max(answer, right-left+1)
    return answer   

