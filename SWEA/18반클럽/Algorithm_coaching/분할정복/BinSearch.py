# 반복구조
# def binary_search(nums, key):
#     low = 0
#     high = len(nums) - 1

#     while low <= high:
#         mid = low + (high - low) // 2  # 10 = 0 + (20 -0) //2
#         if nums[mid] == key:           # nums[10] == key
#             return mid
#         elif nums[mid] > key:          # nums[10] > key
#             high = mid - 1             # 9 = 10 - 1
#         else:
#             low = mid + 1              # 11 = 10 + 1
#     return -1  # 못 찾으면 -1


# 재귀구조
# def binary_search(a, low, high, key):
#     if low > high:
#         return -1
#     else:
#         mid = (low + high) // 2
#         if key == a[mid]:
#             return mid
#         elif key < a[mid]:
#             return binary_search(a, low, mid - 1, key)
#         else:
#             return binary_search(a, mid + 1, high, key)

