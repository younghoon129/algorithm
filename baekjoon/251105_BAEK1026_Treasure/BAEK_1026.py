import sys
sys.stdin = open('BAEK_1026_input.txt', 'r')

n = int(input())
box1 = list(map(int, input().split()))
box2 = list(map(int, input().split()))
s = 0

box1.sort()
box2.sort(reverse=True)

for i in range(n):
    s += box1[i]*box2[i]
print(s)