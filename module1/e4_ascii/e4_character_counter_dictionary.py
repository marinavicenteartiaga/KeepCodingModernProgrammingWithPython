my_text = "three words for you"

frequencies = dict()

for character in my_text:
    if character in frequencies:
        frequencies[character] += 1
    else:
        frequencies[character] = 1

for character in frequencies.keys():
    print(character, "-", frequencies[character])
