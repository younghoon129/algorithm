T = int(input())
 
for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
 
    nums.sort()  # 정렬하고
    carrot = [0]  #
    a = nums[0]  # 정렬한거에 제일 작은 값
    b = 0

    for i in range(n):
        if a == nums[i]:  # 만약 a(정렬한거에 첫번째 값) == nums(정렬 배열) 순회
            carrot[-1] += 1  # carrot 뒤부터 +1
        else:
            carrot.append(1)  # 아니면 carrot 뒤에 1 추가
            a = nums[i]  # a 초기화
    #  =====================================각 숫자의 갯수 구한거 
    
    ans = -1
    nn = len(carrot)  # 당근배열의 갯수
    m_box = []
    s_box = []
    bad_car = n // 2
 
    for i in range(nn):  # 작은 바구니
        s_box.append(carrot[i])
        if sum(s_box) > bad_car:  # 만약 각 사이즈의 당근 다 더한게 기준보다 크면
            break  # 브레이크
        m_box = []  # 초기화

        for j in range(i+1, nn):  # 중간 바구니
            m_box.append(carrot[j])  # s_box 넣은거 제외하고 추가
            if sum(m_box) > bad_car:  # 만약 크면 브레이크
                break  
            
            a = sum(s_box)
            b = sum(m_box)
            c = sum(carrot[j+1:]) # 큰 바구니 m_box 까지 넣은 거 제외하고 추가
             
            if a == 0 or b == 0 or c == 0 or c > bad_car:  # 비어있는 상자가 있으면 pass
                continue   
  
            aaa = max(a, b, c) - min(a, b, c)
            if ans == -1:
                ans = aaa
            else:
                ans = min(ans, aaa)
 
    print (f"#{tc} {ans}")
