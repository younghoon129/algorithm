a = input()
b = input()
result = 0

for i in range(len(b)-1, -1, -1):
    num = int(a)*int(b[i])
    print(num)
    result += num*(10**(len(b)-1-i))
print(result)  