word = input()

length = len(word)

half_index = int(length / 2)

new_word = ''
for i in range(half_index):
    new_word += word[i]
    new_word += word[length - (1 + i)]

if not length % 2 == 0:
    new_word += word[half_index]

print(new_word)