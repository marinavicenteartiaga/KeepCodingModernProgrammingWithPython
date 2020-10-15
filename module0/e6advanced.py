qualifications = (2, 4, 6, 8)

sum = 0
index = 0

while index < len(qualifications):
    sum = sum + qualifications[index]
    index = index + 1

media = sum / index

print("Number of items:", index)
print("Final qualification........", sum)
print("Media........", media)
