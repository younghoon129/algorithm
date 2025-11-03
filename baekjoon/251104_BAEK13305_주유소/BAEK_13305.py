import sys
sys.stdin = open('BAEK_13305_input.txt', 'r')

n = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))
# oil.pop()
cnt = 0
coin = 0
i = 0 # 기름
j = 0 # 길
while j < len(road):
    print(road[j])
    if cnt < road[j]:
        cnt += 1
        coin += oil[i]
        continue
    if oil[i] < oil[i+1]:
        cnt = 0
        j += 1
        continue
    if oil[i] >= oil[i+1]:
        cnt = 0
        i += 1
        j += 1
        continue
print(coin)


# for i in range(len(road)-1):
#
#     while cnt < road[i]:
#         cnt += 1
#         coin += oil[i]






# 2 3 1
# 5 4 2 1

# 30 - 20 + 16 - 4 + 2
# 24
# 30 - 20 + 8

# 18