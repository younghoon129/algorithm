round = int(input())

for r in range(round):
    a = list(map(int, input().split()))
    a.pop(0)
    b = list(map(int, input().split()))
    b.pop(0)
    result = ''
    a_cnt = 0
    b_cnt = 0

    for i in range(4, 0, -1):
        if a.count(i) != b.count(i):
            if a.count(i) > b.count(i):
                result = 'A'
                
                break
            elif a.count(i) < b.count(i):
                result = 'B'
                break
        if i == 1 and a.count(i) == b.count(i):
               result = 'D'
               
               
               
    print(result)