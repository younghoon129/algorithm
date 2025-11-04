import sys
sys.stdin = open('BAEK_13305_input.txt', 'r')

# n = int(input())
# road = list(map(int, input().split()))
# oil = list(map(int, input().split()))
# cnt = 0
# coin = 0
# i = 0 # 기름
# j = 0 # 길
# k = 1
#
# while j < len(road):
#     if cnt < road[j]:
#         cnt = road[j]
#         coin = coin + (oil[i]*road[j])
#     if oil[i] < oil[i+k]:
#         k += 1
#         cnt = 0
#         j += 1
#         continue
#     if oil[i] >= oil[i+k]:
#         cnt = 0
#         i += k
#         j += 1
#         k = 1
#         continue
#
# print(coin)


n = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

tt = 0
ans = 0
while tt < n-1:
    num = 0
    for i in range(tt+1, n):
        num += road[i-1]
        if oil[i] <= oil[tt] or i == n-1:
            ans += oil[tt] * num
            tt = i
            break
print(ans)