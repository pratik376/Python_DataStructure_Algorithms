def minimumMboque(bloomDay, k, m):
    
    l, r= min(bloomDay), max(bloomDay)

    ans= -1

    if k * m > len(bloomDay):
        return -1
    
    while l <= r:
        mid= (l+r)//2

        no_of_adujst, number_boque=0,0

        for val in bloomDay:
            
            if val <= mid:
                no_of_adujst+=1
            else:
                no_of_adujst=0

            if no_of_adujst ==k:
                number_boque+=1
                no_of_adujst=0

        if number_boque>= m:
            r=mid-1
            ans = mid
        else:
            l=mid+1
    return ans                  

               