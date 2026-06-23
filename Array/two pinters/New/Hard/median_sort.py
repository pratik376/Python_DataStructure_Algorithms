def findMedianSortedArrays(nums1, nums2):
    arr = []
    arr.extend(nums1)
    arr.extend(nums2)
    arr.sort()

    n = len(arr)
    mid = n // 2

    if n % 2 == 1:
        return arr[mid]
    else:
        return (arr[mid] + arr[mid - 1]) / 2
