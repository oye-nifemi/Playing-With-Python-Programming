import csv
file = open("Books.csv", "w")
file.write("To Kill A Mockingbird, Harpers Lee, 1960 \n")
file.write("A Brief History Of Time, Stephen Hawking, 1988 \n")
file.write("The Great Gatsby, F. Scott Fitzgerald, 1922 \n")
file.write("The Man Who Mistook His Wife for a Hat , Oliver Sacks, 1985 \n")
file.write("Pride and Prejudice , Jane Austen, 1813 \n")
file.close()

how_many = int(input("Enter the number of books you want to add to the record: "))
while how_many < 0:
    print("Invalid Input.")
    how_many = int(input("Enter the number of books you want to add to the record: "))
for i in range(how_many):
    print("")
    print("Book",i+1,": ")
    book_name = input("Enter the name of the book: ")
    author_name = input("Enter the name of the author: ")
    release_year = input("Enter the year of release: ")
    new_record = book_name + ", " + author_name + ", " + release_year + "\n"
    file = open("Books.csv", "a")
    file.write(str(new_record))
    file.close()
    
file = open("Books.csv", "r")
find_author = input("Enter the author that you seek: ")
count = 0
for row in file:
    if find_author in row:
        print(str(row))
        count += 1
if count == 0:
    print("Author not found")
file.close()