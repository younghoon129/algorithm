# 17:25

n = int(input())
box = list(map(int, input().split()))
s = int(input())
st = []  # 학생, 전구번호 (-1 해야 됨)
result = []  # 결과
for t in range(s):
    st.append(list(map(int,input().split())))

for ch in range(s):  # 학생 수만큼
    bst = st[ch][0]
    if bst == 1:  # 남학생이라면
        bn = st[ch][1] -1
        
        for i in range(bn, len(box), bn+1):
            if box[i] == 1:
                box[i] = 0
            elif box[i] == 0:
                box[i] = 1

    elif bst == 2:  # 여학생이라면
        gn = st[ch][1] - 1
        for j in range(len(box)):
            if 0 <= gn-j and gn+j < len(box):  # 범위
                if box[gn-j] == box[gn+j]:
                    if box[gn+j] == 1:
                        box[gn+j], box[gn-j] = 0, 0
                    elif box[gn+j] == 0:
                        box[gn+j], box[gn-j] = 1, 1
                elif box[gn-j] != box[gn+j]:
                    break

for i in range(0, (len(box)//20)+1):
    if box[20*i:(20*i)+20]:
        result.append(box[20*i:(20*i)+20])
    else:
        result.append(box[20*i:])
for j in range(len(result)):
    print(*result[j])


