def bubbleSort(alist):
    n = len(alist)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
    return alist


alist = [54, 2, 45, 100, 1, 3, 14]
print(bubbleSort(alist))
