# # 14:55 ~ 15: 01
# import sys
# sys.stdin = open("/input.txt", "r")

test = int(input())
for t in range(1, test+1):
    box = input()
    result = ''
    for i in range(1, 11):
        if box[0:i] == box[i:i+i]:
            result = box[0:i]
            break
    print(f"#{t} {len(result)}")