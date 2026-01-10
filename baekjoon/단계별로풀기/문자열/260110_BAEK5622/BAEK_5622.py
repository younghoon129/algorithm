dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

word = input()

total_time = 0

for char in word:
    for i in range(len(dial)):
        if char in dial[i]:
            total_time += (i + 3)
            break

print(total_time)