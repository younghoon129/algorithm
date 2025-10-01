
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
    while left and right:
        if left[-1] > right[-1]:
            cnt +=1
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)

    return result

tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    box = list(map(int, input().split()))
    cnt = 0
    re = merge_sort(box)
    if cnt != 0:
        print(f"#{t} {re[n//2]} {cnt//2}")
    else:
        print(f"#{t} {re[n//2]} {cnt}")

#
# 2
# 5
# 2 2 1 1 3
# 10
# 7 5 4 1 2 10 3 6 9 8