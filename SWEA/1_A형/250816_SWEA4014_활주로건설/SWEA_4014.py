# test = int(input())

# for t in range(1, test+1):
#     n, x = map(int, input().split())
#     box = [list(map(int, input().split())) for _ in range(n)]
#     hwal = 0  # 활주로 가능한 길
#     sb = [max(b) for b in box]
#     # a = box[0].index(1)  # 제일 먼저 나온 인덱스로 반환
#     for i in range(n):
#         cnt = 0
#         b_idx = box[i].index(sb[i])  # 최댓값의 인덱스 (i번줄의 j : 최댓값)
#         for j in range(n):
#             bj = b_idx + j
#             bjm = b_idx - j
#             if bj+1 < n:
#                 if box[i][bj] == box[i][bj+1]+1   # 오른쪽
#                     for k in range(1, n):
#                         bjk = bj*k  # bj = b_idx(최댓값의 인덱스)
#                         if 0 <= bjk < n:
#                             if box[i][bj+1] == box[i][bjk]:
#                                 cnt += 1
#                             elif box[i][bj] != box[i][bjk]:  # 다음 위치 값 다르면
#                                 if cnt % x == 0:

                        
#                     cnt += 1
                




            # if 0 <= bjm:
            #     if    # 왼쪽
            
            









            
            
            # if 0 <= bj < n:
            #     if box[i][b_idx] == box[i][bj]:  # 현재값이랑 다음 값 같으면
            #         cnt += 1  # 
            #     elif box[i][b_idx] > box[i][bj]:  # 현재값 다음 값 다르면
            #         for k in range(1, n):
            #             bjk = bj*k
            #             if 0 <= bjk < n:
            #                 if box[i][bj] == bjk:
            #                     cnt += 1
            #                 elif box[i][bj] != bjk:  # 다음 위치 값 다르면
            #                     if cnt % x == 0:  # 경사로는 놓을 수 있는지 확인하고
            #                           # 놓으면