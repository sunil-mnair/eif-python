vowels = 'aeiou'
count = 0
word = 'programming'

for letter in word:
    #print(letter)
    if letter in vowels:
        print(letter)
        count += 1

print(count)