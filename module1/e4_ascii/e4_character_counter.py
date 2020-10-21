def exists(letter, letter_list):
    pos = 0

    while pos < len(letter_list):
        if letter_list[pos] == letter:
            return pos
        pos += 1

    return None


my_text = "three words for you"

letters = []
frequencies = []

for character in my_text:
    pos = exists(character, letters)
    if pos is not None:
        frequencies[pos] += 1
    else:
        letters.append(character)
        frequencies.append(1)

index = 0
while index < len(letters):
    print(letters[index], "-", frequencies[index])
    index += 1
