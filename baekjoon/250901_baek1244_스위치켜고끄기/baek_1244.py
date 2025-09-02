# 17:25

n = int(input())
box = list(map(int, input().split()))
s = int(input())
st = []  # 학생, 전구번호 (-1 해야 됨)
for t in range(s):
    st.append([map(int,input().split())])

for ch in range(s):
    if st[ch][0] == 1:  # 남학생이라면
        for i in range(st[ch][1]-1, len(box)-1, st[ch][1]):
            if box[i] == 1:
                box[i] = 0
            elif box[i] == 0:   
                box[i] = 1

    elif st[ch][0] == 2:  # 여학생이라면
        gn = st[ch][1] - 1
        for j in range(len(box)-1):
            if 0 <= gn-j and gn+j < len(box):  # 범위

                if box[gn-j] != box[gn+j]:
                    if len(box[gn-j+1:gn+j-1]) == 1:
                        box[gn] =

                elif box[gn-j] == box[gn+j]:
                    continue


