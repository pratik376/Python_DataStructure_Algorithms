def substring(s: str, t: str):

    min=len(s)+1
    substring=""
    end=0
    j=0
    i=0

    while i < len(s):

        if s[i]==t[j]:
            j+=1

            if (j==len(t)):

                end=i+1
                j-=1

                while j>=0:
                    if t[j]==s[i]:
                        j-=1
                    i-=1

                i+=1
                j+=1

                if end-i< min:
                    min=end-i
                    substring=s[i:end]

        i+=1

    return substring                




