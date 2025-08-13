test = int(input())

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

for t in range(1, test+1):
    n = int(input())
    box = [list(map(int, input().split())) for _ in range(n)]
    max_boxnum = max(max(b) for b in box)
    boxidx = [] #[[0, 0]]
    # 최댓값 인덱스
    for i in range(len(box)):
        for j in range(len(box)):
            if box[i][j] == max_boxnum:
                boxidx.append([i, j])

# 시작 지점 인덱스 = boxidx [[0,0], [1,1]]

    for box_l in boxidx:
        A = True
        cnt = 1
        cnts = 0
        while A:              
            n_move = [box_l[0], box_l[1]]
            # print([box_l[0], box_l[1]])
            n_num = []
            n_idx = []
            B = 0
            for f in range(4):
                if 0 <= box_l[0] + dx[f] < n and 0 <= box_l[1] + dy[f] < n:
                    n_num.append(box[n_move[0]+dx[f]][n_move[1]+dy[f]])
                    n_idx.append([n_move[0]+dx[f], n_move[1]+dy[f]])

            # print(n_idx)
            if box[n_move[0]][n_move[1]] < min(n_num):
                cnts += 1
                A = False
            elif box[n_move[0]][n_move[1]] > min(n_num):
                B = n_num.index(min(n_num)) #index
                # print('ddddddddddddddddddddddddd')
                box_l[0], box_l[1] = n_idx[B]
                # print(n_move)
                cnt += 1


        print(f"#{t} {cnt}")
        # max(첫번째, 두번째)
                




# test = int(input())

# dx = [-1, 1, 0 ,0]
# dy = [0, 0, -1, 1]

# for t in range(1, test+1):
#     n = int(input())
#     box = [list(map(int, input().split())) for _ in range(n)]
#     max_boxnum = max(max(b) for b in box)
#     boxidx = [] #[[0, 0]]
#     # 최댓값 인덱스
#     for i in range(len(box)):
#         for j in range(len(box)):
#             if box[i][j] == max_boxnum:
#                 boxidx.append([i, j])

# # 시작 지점 인덱스 = boxidx [[0,0], [1,1]]

#     for box_l in boxidx:
#         A = True
#         cnt = 1
#         cnts = 0
#         while A:               
#             n_move = [box_l[0], box_l[1]]
#             # print([box_l[0], box_l[1]])
#             n_num = []
#             n_idx = []
#             B = 0
#             for f in range(4):
#                 if 0 <= box_l[0] + dx[f] < n and 0 <= box_l[1] + dy[f] < n:
#                     n_num.append(box[n_move[0]+dx[f]][n_move[1]+dy[f]])
#                     n_idx.append([n_move[0]+dx[f], n_move[1]+dy[f]])

#             # print(n_idx)
#             if box[n_move[0]][n_move[1]] < min(n_num):
#                 cnts += 1
#                 A = False
#             elif box[n_move[0]][n_move[1]] > min(n_num):
#                 B = n_num.index(min(n_num)) #index
#                 # print('ddddddddddddddddddddddddd')
#                 box_l[0], box_l[1] = n_idx[B]
#                 # print(n_move)
#                 cnt += 1


#         print(f"#{t} {cnt}")
#         # max(첫번째, 두번째)