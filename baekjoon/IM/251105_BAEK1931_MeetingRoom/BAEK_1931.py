import sys
sys.stdin = open('BAEK_11399_input.txt', 'r')

n = int(input())

box = list(map(int, input().split()))
box.sort()
total = 0
cnt = 0
for i in box:
    cnt += i
    total += cnt
print(total)