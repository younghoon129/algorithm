import sys
sys.stdin = open('MergeSort_input.txt', 'r')
from collections import deque
def merge_sort(arr):
    global cnt
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge(left_half, right_half)

def merge(left, right):
    global cnt
    result = []
    left = deque(left)
    right = deque(right)
    while left and right:
        if left[0] > right[0]:
            result.append(right.popleft())
        else:
            result.append(left.popleft())
    if left:
        # print(result)
        cnt += 1
    result.extend(left)
    result.extend(right)
    # print(result)
    return result

tc = int(input())

for t in range(1, tc+1):
    n = int(input())
    box = list(map(int, input().split()))
    cnt = 0
    re = merge_sort(box)
    print(f"#{t} {re[n//2]} {cnt}")

#
# from collections import deque
#
# def merge_sort(arr):
#     global cnt
#     n = len(arr)
#     if n <= 1:
#         return arr
#     mid = n // 2
#
#     left_half = merge_sort(arr[:mid])
#     right_half = merge_sort(arr[mid:])
#
#     return merge(left_half, right_half)
#
# def merge(left, right):
#     global cnt
#     result = []
#     left = deque(left)
#     right = deque(right)
#
#     while left and right:
#         if left[-1] > right[-1]:   # 문제에서 주어진 비교 조건
#             cnt += 1
#         if left[0] < right[0]:
#             result.append(left.popleft())
#         else:
#             result.append(right.popleft())
#
#     result.extend(left)
#     result.extend(right)
#     return result
#
# tc = int(input())
# for t in range(1, tc+1):
#     n = int(input())
#     box = list(map(int, input().split()))
#     cnt = 0
#     re = merge_sort(box)
#     if cnt != 0:
#         print(f"#{t} {re[n//2]} {cnt//2}")
#     else:
#         print(f"#{t} {re[n//2]} {cnt}")
