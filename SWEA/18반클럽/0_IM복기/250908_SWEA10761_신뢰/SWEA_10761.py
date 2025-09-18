import sys
sys.stdin = open('C://Users//SSAFY//Desktop//김영훈//algorithm//SWEA//18반클럽//0_IM복기//250908_SWEA10761_신뢰//SWEA10761_신뢰.txt', 'r')
test = int(input())
for t in range(1, test+1):
    box = list(input().split())
    b = []  # 숫자
    o = []  # 숫자
    cnt = 1

    
    for i in range(int(box[0])):
        if box[(2*i)+1] == 'B':
            b.append(int(box[2*(i+1)]))
        elif box[(2*i)+1] == 'O':
            o.append(int(box[2*(i+1)]))
    i = 0
    j = 0
    b_road = 0
    o_road = 0
    end_num = max(max(b), max(o))
    while b_road != b[-1] and o_road != o[-1]:
        b_road += 1
        o_road += 1
        print(i, j)
        if i < len(b):
            if b[i] == b_road and o[j] == o_road:
                cnt+=1
                b[i] == 0
                print('1번')
                continue
            if b[i] == b_road:
                cnt+=1
                j+=1
                print('2번')

                continue
            if o[j] == o_road:
                cnt+=1
                i+=1
                print('3번')
                continue
            cnt+=1
            continue
        if j < len(o):
            if o[j] == o_road:
                cnt+=1

                print('4번')
                continue
            cnt+=1
    print(cnt, '나 씨엔티요')
            

        

    # for j in range()

    # for j in range(1, max(m)+1):
