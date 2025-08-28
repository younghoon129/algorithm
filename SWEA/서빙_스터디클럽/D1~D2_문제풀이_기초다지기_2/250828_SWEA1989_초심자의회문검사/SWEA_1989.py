# # 15:11 ~ 15
# import sys
# sys.stdin = open("/input.txt", "r")

test = int(input())
for t in range(1, test+1):
    box = input()
    if box[0:] == box[::-1]:
        print(f"#{t} 1")
    else:
        print(f"#{t} 0")
