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

if month == 1:
    passedDays = day

if month == 2:
    passedDays = 31 + day

if month == 3:
    passedDays = 31 + 28 + day

if month == 4:
    passedDays = 31 + 28 + 31 + day

if month == 5:
    passedDays = 31 + 28 + 31 + 30 + day

if month == 6:
    passedDays = 31 + 28 + 31 + 30 + 31 + day

if month == 7:
    passedDays = 31 + 28 + 31 + 30 + 31 + 30 + day

if month == 8:
    passedDays = 31 + 28 + 31 + 30 + 31 + 30 + 31 + day

if month == 9:
    passedDays = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + day

if month == 10:
    passedDays = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + day

if month == 11:
    passedDays = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + day

if month == 12:
    passedDays = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + day


probability = passedDays / 365 * 100
birthYear = year - age

print("Well,", name, "you were born in", birthYear, ", with a probability of", probability)
print("or in", birthYear - 1, "with a probability of", 100 - probability)
