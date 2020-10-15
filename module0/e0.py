name = input("What's your name?\n")
print("Hello " + name + "!")

strAge = input("How old are you?\n")
strYear = input("What year is it?\n")

strBirthdayYet = input("Has it already been your birthday? (YES/NO)\n")

age = int(strAge)
year = int(strYear)

while strBirthdayYet != "YES" or strBirthdayYet != "NO":
    strBirthdayYet = input("Error. Has it already been your birthday? (YES/NO)\n")
    if strBirthdayYet == "YES":
        birthYear = year - age
        break
    elif strBirthdayYet == "NO":
        birthYear = year - age - 1
        break

if strBirthdayYet == "YES":
    birthYear = year - age
elif strBirthdayYet == "NO":
    birthYear = year - age - 1

print("You were born in ", birthYear)
