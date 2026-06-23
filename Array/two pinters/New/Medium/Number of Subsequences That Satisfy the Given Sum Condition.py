def subsequence(arr, target):

    arr.sort()

    l,r=0,len(arr)-1
    sum=0

    while(l<=r):

        if arr[l]+arr[r] <= target:

            sum+= 2 ** (r-l)
            l+=1
        else :
            r-=1
    return sum        


def numSubseq(arr, target):
    arr.sort()
    l, r = 0, len(arr)-1
    count = 0
    mod = 10**9 + 7

    while l <= r:
        if arr[l] + arr[r] <= target:
            count = (count + pow(2, r-l, mod)) % mod
            l += 1
        else:
            r -= 1

    return count