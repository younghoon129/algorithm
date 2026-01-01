a = input().strip()

box = [-1] * 26

for idx, char in enumerate(a):
    if box[ord(char) - ord('a')] == -1:
        box[ord(char) - ord('a')] = idx

print(*box)