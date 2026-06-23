from collections import defaultdict
# its not number of substrings its longest length one substring that's why we use tradition sliding window if it were total number of substrings then we have to use that atmost(k)- atmost(k-1) 
#Longest substring/array → only care about max length, so max()
#Number of substrings/subarrays → care about count of all valid subarrays, so +=

def longestSubstring(str,k):

    dict=defaultdict(int)
    left=0
    length= float('-inf')


    for right in range(len(str)):

        dict[str[right]]+=1

        while len(dict) > k:

            dict[str[left]]-=1

            if dict[str[left]]==0 :
                del dict[str[left]]

            left+=1

        length=max(length, right-left+1)   

    return length         


    

