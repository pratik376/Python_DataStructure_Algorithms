def maxConsecutive(arr,k):

    left=0
    count= k
    answer=0


    for right in range(len(arr)):

        if arr[right]==0:
            count-=1


        while count==-1: # or count < 0

            if arr[left]==0:
                count+=1
            left+=1
        answer= max(answer, right-left+1)
    return answer        



