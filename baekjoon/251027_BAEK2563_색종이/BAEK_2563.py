import sys
sys.stdin = open('BAEK_2563_input.txt', 'r')
from pprint import pprint
def put(h, y):
    global box
    a = n-1-h
    for i in range(a, a-p_size, -1):
        for j in range(y, (y + p_size)):
            box[i][j] = 1

def find_one(box):
    global result
    result += sum(map(sum, box))

result = 0
n = 100
paper = int(input())
p_size = 10
box = [[0] * n for _ in range(n)]

for i in range(paper):
    x, y = map(int, input().split())
    put(y, x)
find_one(box)
print(result)
