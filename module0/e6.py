qualifications = (2, 4, 6, 8)

def content(items, index):
    try:
        result = items[index]
    except:
        result = None

    return result

def length(items):
    index = 0
    while content(items, index) != None:
        index = index + 1

    return  index

sum = 0

for index in range(0, length(qualifications)):
    sum = sum + qualifications[index]

media = sum / length(qualifications)

print("Number of items:", length(qualifications))
print("Final qualification........", sum)
print("Media........", media)
