from collections import deque
# d = deque()
# d.extend([1,2,3,4,5,6])
# d.append(d.popleft())
# print(d)
def turn_mag(mag1, mag2, mag3, mag4, x, y, mag_sum):  # x : 자석번호, y : 회전방향
    
    pass






tc = int(input())
for t in range(1, tc+1):
    magnetic = 4
    nn = int(input())
    mag1 = list(map(int, input().split()))
    mag2 = list(map(int, input().split()))
    mag3 = list(map(int, input().split()))
    mag4 = list(map(int, input().split()))
    mag_sum = 0
    result = 0
    for n in range(nn):
        x, y = map(int, input())
        turn_mag(mag1, mag2, mag3, mag4, x, y, mag_sum)
        result += mag_sum
    

# 1
# 1
# 0 0 1 0 0 1 0 0
# 1 0 0 1 1 1 0 1
# 0 0 1 0 1 1 0 0
# 0 0 1 0 1 1 0 1