# 23: 04 ~ 23 : 38
test = int(input())
cal = {
    '01' : 31,
    '02' : 28,
    '03' : 31,
    '04' : 30,
    '05' : 31,
    '06' : 30,
    '07' : 31,
    '08' : 31,
    '09' : 30,
    '10' : 31,
    '11' : 30,
    '12' : 31
    }
for t in range(1, test+1):
    n = input()
    box = [0]*3
    box[0] = n[0:4]
    box[1] = n[4:6]
    box[2] = n[6:]
    if 1 <= int(box[1]) <= 12:
        if 1 <= int(box[2]) <= cal[box[1]]:
            print(f"#{t} {'/'.join(box)}")
        else:
            print(f"#{t} -1")
    else:
        print(f"#{t} -1")