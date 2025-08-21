# import sys
# sys.stdin = open("1974_input.txt", "r")

T = int(input())
for test_case in range(1,T+1):
    sdok = [list(map(int,input().split())) for _ in range(9)]
    cnt = 1
    for i in range(9):
        box_i = [0]*10
        box_j = [0]*10
        box_k = [0]*10
        for j in range(9):
            box_i[sdok[i][j]] += 1
            box_j[sdok[j][i]] += 1
        
        for k in range(1, 10):
            if box_i[k] != 1:
                cnt = 0
                break
            if box_j[k] != 1:
                cnt = 0
                break

    # for i in range(9):
    #     for j in range(9):
    #         num = 0
    #         if sum(sdok[i][0:9]) != 45 and sum(sdok[0:9][j]) != 45:
    #             cnt = 0
    #             break
        if i % 3 == 0 and j % 3 == 0:
            for l in range(i, i+3):
                for o in range(j, j+3):
                    box_k[sdok[l][o]] += 1
            for p in range(1, 10):
                if box_k[p] != 1:
                    cnt = 0
                    break
        if cnt == 0:
            break
    #             else:
    #                 if num != 45:
    #                     cnt = 0
    #                     break
    
    #     if cnt == 0:
    #         break
    print(f"#{test_case} {cnt}")

    