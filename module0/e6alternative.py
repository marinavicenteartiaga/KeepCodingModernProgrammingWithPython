qualifications = (2, 4, 6, 8)

sum = 0
leng_qualifications = len(qualifications)

for index in range(0, leng_qualifications):
    sum = sum + qualifications[index]

media = sum / leng_qualifications

print("Number of items:", leng_qualifications)
print("Final qualification........", sum)
print("Media........", media)
