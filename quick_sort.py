import math
import random
from typing import List


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


def quick_perm(arr):
    if len(arr) < 2:
        return [arr]
    perm_list = []
    for i in arr:
        remaining_elements = [x for x in arr if x != i]
        for perm in quick_perm(remaining_elements):
            perm_list.append([i] + perm)
    return perm_list


if __name__ == '__main__':
    res = random.sample(range(1, 50), 7)
    print(res)
    print(quick_sort(res))
    for line in quick_perm(res):
        print(line)
