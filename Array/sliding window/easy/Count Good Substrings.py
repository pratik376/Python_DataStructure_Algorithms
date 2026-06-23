from collections import defaultdict

def countGoodString(s):

    count=defaultdict(int)

    if len(s)<3:
        return 0

    window_sum=0
    
    left=0 
    for i in range(3):

        count[s[i]]+=1

    window_sum +=1 if len(count)==3 else 0  


    for right in range(3,len(s)):

        count[s[right]]+=1
        count[s[left]]-=1

        if count[s[left]]==0:
            del count[s[left]]

        left +=1      

        window_sum +=1 if len(count)==3 else 0  

    return window_sum     

