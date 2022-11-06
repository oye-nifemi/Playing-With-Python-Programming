import csv

file = open("fellow.csv", "w")
new_record = "Barry, 73, Ondo\n"
file.write(str(new_record))
file.close()

file = open("fellow.csv", "a")
name = input("Enter new name: ")
age = input("Enter age: ")
state = input("Enter state of origin: ")
new_record = name + ", " + age + ", " + state
file.write(new_record)
file.close()

# file = open("fellow.csv", "r")
# for row in file:
#     print(row)
    
file = open("fellow.csv",'r')
reader = csv.reader(file)
rows = list(reader)
print(rows[0]) 