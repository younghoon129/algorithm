test = int(input())
for t in range(1, test+1):
    n, m = map(int, input().split())
    str_list = [list(map(str, input())) for _ in range(n)]
    for i in range(n):
        for j in range(n-m+1):
            l_str = ''
            r_str = ''
            sum_str = ''
            print(n, m, j, j+m)
            if (i+m-1) < n and (j+m-1) < n:
                if str_list[i][j] == str_list[i][j+m-1]: # (j+m) = 19, n = 20
                    # 격자 안에 있고, 첫글자 끝 글자 같다면
                    print("if문 들왔음")
                    for k in range((m//2)-1):  # m//2 만큼 양쪽에서 가운데까지 이동
                        print('k 들어 왓음')
                        if str_list[i][j+k] == str_list[i][j+m-k-1]:
                            print('k 안에 if 들어왓음')
                            l_str += str_list[i][j+k]
                            r_str += str_list[i][j+m-k]
                        else:
                            print('k 안에 else')
                            break
                    else:
                        print('for else 썻음 for문 정상 끝나면 실행')
                        if l_str == r_str and m % 2 == 1:
                            print('for else 안에 if')
                            # print(l_str + str_list[i][j] + r_str)
                            sum_str = l_str+str_list[i][j+(m//2)]+r_str
                        # elif(str_list[i][j+k] != str_list[i][j+m-k]):
                        #     break
        print(sum_str)
















 # if m % 2 == 0:
                #     for l in range(m // 2):  # m//2 만큼 양쪽에서 가운데까지 이동
                #
                #         l_str += str_list[i][j+l]
                #         r_str += str_list[i][j+m-l]
                #         print(l_str, r_str, '짝수일때')