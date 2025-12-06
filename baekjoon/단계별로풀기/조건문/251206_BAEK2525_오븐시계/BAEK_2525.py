A, B = map(int, input().split())
C = int(input())

B += C 
A += B // 60
B = B % 60

A = A % 24

print(A, B)