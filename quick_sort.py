import math
import random


def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        if arr[i] >= pivot:
            right.append(arr[i])
    return quick_sort(left) + [pivot] + quick_sort(right)


def quick_perm(arr: list[int]) -> list[int]:
    if len(arr) < 2:
        return arr
    for i in range(1, len(arr)):
        print(arr[i] + quick_perm())



if __name__ == '__main__':
    res = random.sample(range(1, 50), 7)
    print(res)
    print(quick_sort(res))
