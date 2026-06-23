from collections import deque

def maximumWindow(arr, k):
    q = deque()
    answer = []

    for r in range(len(arr)):

        # 1. Remove elements outside window
        if q and q[0] <= r - k:
            q.popleft()

        # 2. Maintain decreasing deque
        while q and arr[q[-1]] < arr[r]:
            q.pop()

        q.append(r)

        # 3. Add result when window is valid
        if r >= k - 1:
            answer.append(arr[q[0]])

    return answer


arr = [1,3,-1,-3,5,3,6,7]
k = 3
print(maximumWindow(arr, k))

