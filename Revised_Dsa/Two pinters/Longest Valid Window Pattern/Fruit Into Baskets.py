from collections import defaultdict
def fruitsIntoTheBaske(arr):

    left=0
    basket= defaultdict(int)
    answer=0

    for right in range(len(arr)):

        basket[arr[right]]+=1


        while len(basket)>2:

            basket[arr[left]]-=1

            if basket[arr[left]] == 0:
                del basket[arr[left]]

            left+=1
        answer=max(answer, right-left+1)
    return answer        
                