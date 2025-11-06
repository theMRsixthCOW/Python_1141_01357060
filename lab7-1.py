# tinsort is faster

def QuickSort(arr):
    n = len(arr)
    
    left = []
    right = []
    pivot = arr[0]

    for i in range(1, n):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return QuickSort(left) + [pivot] + QuickSort(right)

table = list(map(int, input().strip().split()))

sorted_table = QuickSort(table)

print(' '.join(map(str, sorted_table)))