daysInMonths = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30)

name = input("What's your name?\n")
print("Hello " + name + "!")

strAge = input("How old are you?\n")
strDay = input("What day is it? (number ex: 22)\n")
strMonth = input("What month is it? (number ex: 1)\n")
strYear = input("What year is it?(number ex: 2020)\n")


age = int(strAge)
day = int(strDay)
month = int(strMonth)
year = int(strYear)

passedDays = 0
index = 0

while index < month - 1:
    passedDays = passedDays + daysInMonths[index]
    index = index + 1


probability = passedDays / 365 * 100
birthYear = year - age

print("Well,", name, "you were born in", birthYear, ", with a probability of", probability)
print("or in", birthYear - 1, "with a probability of", 100 - probability)
