def my_upper(message):
    result = ""

    for character in message:
        character_code = ord(character)
        if 97 <= character_code <= 122:
            capital_code = character_code - 32
            capital_character = chr(capital_code)
            result = result + capital_character
        else:
            result = result + character

    return result


words = input("Say something whispering: ")
print("I shout to you:", my_upper(words))
