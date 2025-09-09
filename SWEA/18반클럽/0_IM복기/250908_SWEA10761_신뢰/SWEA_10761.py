test = int(input())
for t in range(1, test+1):
    box = list(input().split())
    b = []  # 문자
    o = []  # 숫자
    b_cnt = 1
    o_cnt = 1
    bm = 0
    om = 0
    for i in range(int(box[0])):
        if box[(2*i)+1] == 'B':
            b.append([box[(2*i)+1],box[2*(i+1)]])
            print([box[(2*i)+1],box[2*(i+1)]], i)
        elif box[(2*i)+1] == 'O':
            o.append([box[(2*i)+1],box[2*(i+1)]])
            print([box[(2*i)+1],box[2*(i+1)]], i)

    for mb in b:
        bm = max(bm, int(mb[1]))
    for mo in o:
        om = max(om, int(mo[1]))
    mm = max(bm, om)
    
    
    
    # for j in range()

    # for j in range(1, max(m)+1):
