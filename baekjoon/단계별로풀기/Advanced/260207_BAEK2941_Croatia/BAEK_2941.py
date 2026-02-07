croatian_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for alpha in croatian_alphabets:
    word = word.replace(alpha, '*')

print(len(word))