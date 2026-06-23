from collections import defaultdict
def minwindow(str, t):


    if t == "": return " "
    left=0
    res, resLen= [-1,-1], float('inf')
    have, need = 0,0

    countT, window= defaultdict(int),defaultdict(int)

    for c in t:
        countT[c]+=1

    need= len(countT)


    for r in range(len(str)):

        window[str[r]]+=1

        if str[r] in countT and window[str[r]] == countT[str[r]]:
            have+=1

        while have == need:

            if (r-left+1) < resLen:
                res=[left,r]
                resLen= r-left+1

            window[str[left]]-=1     

            if str[left] in countT and window[str[left]] < countT[str[left]]:
                have-=1

            left+=1
    left,r =res        

    return str[left:r+1] if resLen != float('infinity') else ""
            





