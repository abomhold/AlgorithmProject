import math
import random
import sys
from typing import Any


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


def quick_perm(arr: list[Any]) -> list[list]:
    if len(arr) < 2:
        return [arr]
    perm_list = []
    for i in arr:
        remaining_elements = [x for x in arr if x != i]
        for perm in quick_perm(remaining_elements):
            perm_list.append([i] + perm)
    return perm_list


def distance(a: int, b: int):
    return math.fabs(a - b)


def held_karp(arr, pos, mask, memo):
    # Check if all nodes have been visited
    if mask == 2 ** len(arr) - 1:
        return distance(arr[pos], arr[0])

    if memo.__contains__((pos, mask)):
        return memo[(pos, mask)]

    ans = float('inf')

    for i in range(1, len(arr)):
        if (mask >> i) == 0:
            ans = min(ans, held_karp(arr, i, (mask | 1 << i), memo) + distance(arr[pos], arr[i]))
    memo[(pos, mask)] = ans
    return ans


if __name__ == '__main__':
    # res = random.sample(range(1, 50), 7)
    res = [13, 23, 7, 29, 24, 22, 26]
    print(res)
    print(quick_sort(res))
    memo: dict = {}
    print(held_karp(res, 0, 1, memo))

    # print(quick_sort(res))
    # for line in quick_perm(res):
    #     print(line)
