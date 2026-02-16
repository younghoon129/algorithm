n = int(input())
current_max = 1
count = 1
while n > current_max:
    current_max += 6 * count
    count += 1
print(count)