...
def isAnagram(word_1, word_2):
    first_word = word_1.upper()
    second_word = word_2.upper()
    if len(first_word) == len(second_word):
        for character in first_word:
            index = second_word.find(character)
            second_word = second_word[:index] + second_word[index+1:]
        if second_word == "":
            return True
    return False


...


def count_characters(str):
    result = dict()

    for character in str:
        if character in result:
            result[character] += 1
        else:
            result[character] = 1
    return result


def is_anagram(w1, w2):
    dw1 = count_characters(w1)
    dw2 = count_characters(w2)

    if len(dw1) != len(dw2):
        return False

    for character in dw1:
        if character in dw2 and dw1[character] == dw2[character]:
            pass
        else:
            return False

    return True


word1 = input("First word: ")
word2 = input("Second word: ")

if isAnagram(word1, word2):
    print(word1, "and", word2, "are anagrams!!")
else:
    print(word1, "and", word2, "are not anagrams!!")
