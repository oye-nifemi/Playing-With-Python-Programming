file = open("Countries.txt", "w")
file.write("Nigeria\n")
file.write("Ghana\n")
file.write("Egypt\n")
file.write("Cameroon\n")
file.close()

file = open("Countries.txt", "r")
print(file.read())
file.close()



# Write a new file called “Numbers.txt”. Add five numbers to the document which are stored on the same line and only separated by a comma. Once you have run the program, look in the location where your program is stored and you should see that the file has been created. The easiest way to view the contents of the new text file on a Windows system is to read it using Notepad.
file = open("Numbers.txt", "w")
file.write("1 ")
file.write("2 ")
file.write("3 ")
file.write("4 ")
file.write("5 ")
file.close()



# Program to get user to input what to be stored in the file
entry = int(input((" 1) Create a new file\n 2) Display the file\n 3) Add a new item to the file\n\n Make a selection: 1, 2, or 3: ")))

if entry == 1:
    school_subject = input("Enter a school subject: ")
    file = open("Subject.txt", "w")
    file.write(school_subject)
    file.write("\n")
    file.close()
elif entry == 2:
    file = open("Subject.txt", "r")
    print(file.read())
elif entry == 3:
    entry = input("Enter the item that you want to add: ")
    file = open("Subject.txt", "a")
    file.write(entry)
    file.close()
else:
    print("Invalid Input.")