test = int(input())
for t in range(1, test+1):
    n, m = map(int, input().split())
    str_list = [list(map(str, input().split())) for _ in range(n)]
    for i in range(n):
        # Lr_str = ''
        print('첫 포문')
        for j in range(n-m+1):
            print('2 포문')
            l_str = ''
            r_str = ''
            sum_str = ''
            print(j+m, n)
            print(j)
            if (j+m-1) <= n-1 and str_list[i][j] == str_list[i][j+m-1]:
                print('격자크기 확인')

                for k in range(m//2):  # m//2 만큼 양쪽에서 가운데까지 이동
                    
                    l_str += str_list[i][j+k]
                    r_str += str_list[i][j+m-k]
                    
                    if 

                    elif(str_list[i][j+k] != str_list[i][j+m-k]):
                        break                        

                else:
                    if l_str == r_str and m%2 == 0:
                        # print(l_str+r_str)
                        sum_str = l_str+r_str
                    if l_str == r_str and m%2 == 1:
                        # print(l_str + str_list[i][j] + r_str)
                        sum_str = l_str+str_list[i][j]+r_str
    print(sum_str)
















 # if m % 2 == 0:
                #     for l in range(m // 2):  # m//2 만큼 양쪽에서 가운데까지 이동
                #
                #         l_str += str_list[i][j+l]
                #         r_str += str_list[i][j+m-l]
                #         print(l_str, r_str, '짝수일때')