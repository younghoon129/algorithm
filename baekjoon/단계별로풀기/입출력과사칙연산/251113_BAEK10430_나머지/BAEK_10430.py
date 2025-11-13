a, b, c = map(int, input().split())
num1 = (a+b)%c
num2 = ((a%c)+(b%c))%c
num3 = (a*b)%c
num4 = ((a%c)*(b%c))%c
print(num1)
print(num2)
print(num3)
print(num4)