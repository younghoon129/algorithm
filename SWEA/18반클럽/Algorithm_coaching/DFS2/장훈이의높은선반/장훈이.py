from itertools import combinations
# def dfs(arr, n):
#     result = 100  # 조합을 저장할 리스트

#     if n == 1:
#         return [[i] for i in arr]

#     for i in range(len(arr)):
#         elem = arr[i]

#         for rest in dfs(arr[i + 1:], n - 1):  # 조합
#             if bs - [elem] + rest >= b:
#                 result = min(result, bs - [elem] + rest)


#     return result


# test = int(input())

# for t in range(1, test+1):
#     n, b = map(int, input().split())
#     box = list(map(int, input().split()))
#     bs = sum(box)

# for i in range(n):
#     print(dfs(box, i))
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# T = int(input())
# for test_case in range(1, T+1):
#     N, B = map(int, input().split())
#     arr = list(map(int, input().split()))

#     min_height = float('INF')

#     for r in range(1, N+1):
#         comb_list = combinations(arr, r)
#         for comb in comb_list:
#             total_height = sum(comb)

#             if total_height >= B:
#                 total_height = min(total_height, min_height)
    
#     print(f"#{test_case} {total_height-B}")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# T = int(input())
# for test_case in range(1, T+1):
#     N, B = map(int, input().split())
#     arr = list(map(int, input().split()))

#     min_height = float('INF')

#     def dfs(idx, h_sum):
#         global min_height
#         if h_sum >= min_height:
#             return
#         if idx == N:
#             if h_sum >= B:
#                 min_height = min(min_height, h_sum)
#             return
        
#         dfs(idx+1, h_sum+arr[idx])


#         dfs(idx+1, h_sum)
    
#     dfs()
    # 2시간10분쯤 다시보기

    