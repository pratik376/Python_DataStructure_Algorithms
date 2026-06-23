from collections import defaultdict
def lonestRepeating(string, k):

    res=0
    left=0

    count=defaultdict(int)


    for right in range(len(string)):

        count[string[right]]+=1


        while (right-left+1) - max(count.values()) >k:

            count[string[left]]-=1

            if count[string[left]] ==0:
                del count[string[left]]

            left+=1
        res= max(res, right-left+1)
    return res           


# or

from collections import defaultdict

def longestRepeating(string, k):

    count = defaultdict(int)
    left = 0
    max_freq = 0
    res = 0

    for right in range(len(string)):

        count[string[right]] += 1
        max_freq = max(max_freq, count[string[right]])

        while (right - left + 1) - max_freq > k:
            count[string[left]] -= 1
            left += 1

        res = max(res, right - left + 1)

    return res