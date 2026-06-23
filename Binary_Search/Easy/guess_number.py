def guess():
    pass

def guessnumber(self, n: int):

    l, r=1,n

    while l<=r:

        mid= (l+r)//2

        token= guess(mid)

        if token == -1:
            r=mid-1
        elif token == 1:
            l=mid+1
        else:
            return mid
                    