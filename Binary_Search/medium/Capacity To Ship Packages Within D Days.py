def Capicity(arr, days):

    l,r= max(arr), sum(arr)

    answer= float('inf')


    while l< r:


        capicity= (l+r)//2
        weight=0
        days_needed=1

        for i in range(len(arr)):
            val=arr[i]

            if weight >= capicity:
                days_needed+=1
                weight=0
            else:
                weight+=val

        answer=min(answer,capicity)

        if days_needed<=days:
            r=capicity-1
        else:
            l=capicity+1



    return answer    

# this is right answer
#                 

def capacity(arr, days):

    l, r = max(arr), sum(arr)
    result = r

    while l <= r:

        mid = (l + r) // 2

        days_needed = 1
        weight = 0

        for val in arr:
            if weight + val > mid:
                days_needed += 1
                weight = val
            else:
                weight += val

        if days_needed <= days:
            result = min(result, mid)
            r = mid - 1
        else:
            l = mid + 1

    return result




