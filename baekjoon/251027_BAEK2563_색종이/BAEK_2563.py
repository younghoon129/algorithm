import sys
sys.stdin = open('BAEK_2563_input.txt', 'r')

def put(h, y):
    global box
    for i in range((n - 1 - h), (n - 1 - h - p_size)):
        for j in range(y, (y + p_size)):



n = 100
paper = int(input())
p_size = 10
box = [[0] * n for _ in range(n)]


for i in range(paper):
    x, y = map(int, input().split())
    put(y, x)