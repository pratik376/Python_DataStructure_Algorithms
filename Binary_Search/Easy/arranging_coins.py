def arrangingCoins(n):
    l, r = 1, n
    res = 0

    while l <= r:
        mid = (l + r) // 2
        num_coins = (mid * (mid + 1)) // 2

        if num_coins > n:
            r = mid - 1
        else:
            res = mid
            l = mid + 1

    return res