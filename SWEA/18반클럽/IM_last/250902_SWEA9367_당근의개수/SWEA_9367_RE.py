import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\git\\algorism\\SWEA\\18반클럽\\IM_last\\250902_SWEA9367_당근의개수\\carrot_input.txt','r')

# 같은 크기 당근은 같은 상저ㅏ
# 비어있는 상자x
# 한 상자에 n/2 초과 x
tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    box = list(map(int, input().split()))
    # min_num = float('inf')
    # carrot = [[], [], []]
    # for i in range(len(box)):
    #     carrot[0].append(box[i])
    # for j in range():
    box.sort()
    carrot = [0]
    a = box[0]
    b = 0

    for i in range(n):
        if a == box[i]:  # 가장 작은값부터 순회할건데 값이 같으면
            carrot[-1] += 1  # carrot 뒤에 +1
        else:
            carrot.append(1)  # 다르면 carrot 길이 하나 더 추가
            a = box[i]  # 그 다음 작은 값으로 초기화

    ans = -1
    l_box = []
    r_box = []
    bl = n // 2
    for i in range(len(carrot)):
        l_box.append(carrot[i])
        if sum(l_box) > bl:
            break
        r_box = []
        for j in range(i+1, len(carrot)):
            r_box.append(carrot[j])
            if sum(r_box) > bl:
                break
            a = sum(l_box)
            b = sum(r_box)
            c = sum(carrot[j+1:])
            if a == 0 or b == 0 or c == 0 or c > len(bl):
                continue
            aaa = max(a, b, c) - min(a, b, c)
            # if ans == -1:
            #     ans = aaa
            ans = min(ans, aaa)

    print(f"#{tc} {ans}")
