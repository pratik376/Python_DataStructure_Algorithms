def missingElement(arr, k):

    n = len(arr)

    def missing(i):
        return arr[i] - arr[0] - i

    # Case 1: beyond array
    if k > missing(n - 1):
        return arr[-1] + (k - missing(n - 1))

    # Case 2: inside array
    l, r = 0, n - 1

    while l <= r:

        mid = (l + r) // 2

        if missing(mid) < k:
            l = mid + 1
        else:
            r = mid - 1

    return arr[0] + l + k - 1