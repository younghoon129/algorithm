# 22 : 41 ~ 22 : 36
# import sys
# sys.stdin = open("C:/Users/user/Desktop/git/algorism/SWEA/서빙_스터디클럽/D1~D2_문제풀이_기초다지기/250827_SWEA1859_백만장자프로젝트/1859_input.txt", "r")


test = int(input())
for t in range(1, test+1):
    n = int(input())
    box = list(map(int, input().split()))
    mon = [0, 0]  # 갯수, 돈
    cnt = 0
    for i in range(n):
        if box[i] == max(box[i:]):
            cnt += (box[i]*mon[0]) - (mon[1])
            # print(box[i], mon[1], t)
            mon = [0,0]
            continue
        elif box[i] != max(box[i:]):
            mon[0] += 1
            mon[1] += box[i]
    print(f"#{t} {cnt}")

#1 4053
#2 6385
#3 26725
#4 211514
#5 4848198
#6 49761546
#7 500155606
#8 4995241394
#9 4999367498
#10 4995633799
