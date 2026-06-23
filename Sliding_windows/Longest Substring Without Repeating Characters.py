def longestSubstringWithouRepeating(s):

    left=0
    max_length=0
    seen=set()

    for right in range(len(s)):

        if s[right] in seen:
            
                max_length=max(max_length,right-left+1)
                seen.remove[s[left]]
                left+=1
                seen.add(s[right])
        else:
             seen.add(s[right])


    if len(seen) > max_length:
         return len(seen)                 
    else:
         return max_length        


# 

def longestSubstringWithoutRepeating(s):
    left = 0
    max_length = 0
    seen = set()

    for right in range(len(s)):
        while s[right] in seen:       # remove duplicates
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)  # update every iteration

    return max_length
