import csv

genders = {
    "Female": 0,
    "Male": 0
}

with open("biostats.csv", "r") as file:
    # reader = csv.reader(file)
    reader = csv.DictReader(file)
    for row in reader:
        gender = row["Sex"] #value of the "Sex" property in each row is saved to gender one by one
        genders[gender] += 1 #after a new gender value is read & saved in 'gender' variable, count of that gender (female or male) will be increemented by 1

for gender in genders:
    count = genders[gender]
    print(f"{gender}: {count}")
