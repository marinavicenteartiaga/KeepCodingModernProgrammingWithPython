january = 31
february = 28
march = 31
april = 30
may = 31
june = 30
july = 31
august = 31
september = 30
october = 31
november = 30

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

if month > 1:
    passedDays = passedDays + january

if month > 2:
    passedDays = passedDays + february

if month > 3:
    passedDays = passedDays + march

if month > 4:
    passedDays = passedDays + april

if month > 5:
    passedDays = passedDays + may

if month > 6:
    passedDays = passedDays + june

if month > 7:
    passedDays = passedDays + july

if month > 8:
    passedDays = passedDays + august

if month > 9:
    passedDays = passedDays + september

if month > 10:
    passedDays = passedDays + october

if month > 11:
    passedDays = passedDays + november


probability = passedDays / 365 * 100
birthYear = year - age

print("Well,", name, "you were born in", birthYear, ", with a probability of", probability)
print("or in", birthYear - 1, "with a probability of", 100 - probability)
