from collections import defaultdict
def findKlength(str,k):

    left=0
    count=0
    frequency=defaultdict(int)

    for i in range(k):

        frequency[str[i]]+=1

    if len(frequency)==k:
        count+=1


    for right in range(k,len(str)):

        frequency[str[right]]+=1
        frequency[str[left]]-=1

        if not frequency[str[left]]:
            frequency.pop(str[left])

        left+=1

        if len(frequency)==k:
            count+=1

    return count            



        
