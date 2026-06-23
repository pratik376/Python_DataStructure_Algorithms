from collections import deque
def shortestSubArray(arr,k):

    res=float('inf')
    cur_sum=0
    q= deque()

    for r in range(len(arr)):
        cur_sum+= arr[r]

        if cur_sum>= k:

            res=min (res, r+1)

        while q and cur_sum- q[0][0] >= k:
            prefix, end_idx= q.popleft()

            res= min(res, r-end_idx)

        while q and q[-1][0] >cur_sum:  # maintain monotonic nature
            q.pop()

        q.append((cur_sum,r))

    return -1 if res==float('inf') else res            

