n = int(input())

for i in range(n):
    box = input()
    result = ''
    result += box[0]
    result += box[-1]
    print(result)

