import csv

file = open("biostats.csv", "a")

Name = input("Name: ")
Sex = input("Sex: ")
Age = input("Age: ")
Height = input("Height: ")
Weight = input("Weight: ")

writer = csv.writer(file)
writer.writerow([Name, Sex, Age, Height, Weight])

file.close()
