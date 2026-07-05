import heapq

def heap_sort(arr):
    heapq.heapify(arr)

    result = []
    while arr:
        result.append(heapq.heappop(arr))

    return result


nums = [5, 3, 8, 1, 2]
print(heap_sort(nums))