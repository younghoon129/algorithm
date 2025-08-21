# 1:56 시작
# + 10
import sys
sys.stdin = open("4861_input.txt", "r")
test = int(input())

for t in range(1, test+1):
    n, m = map(int, input().split())
    box = [input() for _ in range(n)]
    print(box)
    word = ''
    print(m//2)
    for i in range(n):
        for j in range(n-m+1):
            cnt = 0
            for k in range(m//2):
                jmk = j+m-k-1
                if 0 <= j+k < n and 0 <= jmk < n:
                    if j+k < j+m-k-1:
                        if box[i][j+k] == box[i][jmk]:
                            cnt += 1
                        elif box[i][j+k] != box[i][j+m-k-1]:
                            break
            else:
                if cnt == m//2:
                    for l in range(j, j+m):
                        word += box[i][l]
    print(word)

    # ECFQBK S YBBOSZ
    # for i in range(n):
    #         for j in range(n-m+1):  # 시작 위치
    #             cnt = 0
    #             for k in range(m//2):
    #                 if box[i][j+k] == box[i][j+m-k-1]:
    #                     cnt += 1
    #                 else:
    #                     break
    #             else:  # 회문 발견!
    #                 word = ''.join(box[i][j:j+m])
    #                 break
    #         if word:
    #             break
    # print(word)
