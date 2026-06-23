def firstBadVersion(n):
    l, r = 1, n
    res = n

    while l <= r:
        mid = (l + r) // 2

        if isBadVersion(mid):
            res = mid
            r = mid - 1
        else:
            l = mid + 1

    return res