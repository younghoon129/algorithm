test = int(input())
for t in range(1, test+1):
    n = int(input())
    box = list(map(int, input().split()))
    box.sort()
    s_box = set(box)
    
    l_box = []
    cnt = 0
    result = 0
    for i in s_box:
        l_box.append(box.count(i))
    # 각 숫자 갯수 넣음
    r_box = [0,0,0]

    for i in range(len(r_box)):
        for j in range(len(l_box)):
            if r_box[i] < n//2:
                print(j, l_box, '@@@@@')
                r_box[i] += l_box[j]
                l_box[j] = 0
                if r_box[i] > n//2:
                    cnt = -1
                    break
            elif r_box[i] > n//2:
                cnt = -1
                break
    # for q in range(le)
    while max(r_box)-min(r_box) != 1 or max(r_box)-min(r_box) != 0:
        a = r_box.index(max(r_box))
        b = r_box.index(min(r_box))
        r_box[a] -= 1
        r_box[b] += 1

    result = max(r_box) - min(r_box)
    if cnt == -1:
        print(f"#{t} {cnt}")
    else:
        print(f"#{t} {result}")
