# Printing numbers 1 to 10 on the screen using a list to store the numbers
list = []
for i in range(1,11):
    list.append(i)
print(list)


# Create a tuple with the following elements: 1, 2, 2, 3, 4, 4, 4, 5, and then use the tuple object’s count function to check how many times the number four appears in the tuple
tuple = (1, 2, 2, 3, 4, 4, 4, 5)
print(tuple.count(4))


# Add one more element to the dictionary created
dictionary = {"BMJS":2020, "JNCS":2014, "PAU":2024}
print("This is the initial dictionary:", dictionary)
dictionary["Masters?"] = 2025
print("This is the new dictionary:", dictionary)


# Print on the screen only the characters from position 1 to 18 in the text: 'Data scientist is the sexyest professional of the 21st century'
text = 'Data scientist is the sexyest professional of the 21st century'
print(text[1:19])


# Ask the user to enter their first name and then display the length of their name.
# firstname = input("Enter your firstname: ")
firstname = "Nifemi"
print(len(firstname))


# Pig Latin takes the first consonant of a word, moves it to the end of the word and adds on an “ay”. If a word begins with a vowel you just add “way” to the end. For example, pig becomes igpay, banana becomes ananabay, and aadvark becomes aadvarkway. Create a program that will ask the user to enter a word and change it into Pig Latin. Make sure the new word is displayed in lower case.
word = "NIFEMI"
# word = input("Enter the word of your choice: ")
vowels = ["a", "e", "i", "o", "u"]
if word[0] in vowels:
    print(word + "way")
else:
    pig_latin = word[1:-1] + word[0] + "ay"
    print(pig_latin.lower())
    
    
# If the user enters 1, then it should ask them for the length of one of its sides and display the area. If they select 2, it should ask for the base and height of the triangle and display the area. If they type in anything else, it should give them a suitable error message. 
print("1) Square \n2) Triangle")
# number = float(input("Enter a number: "))
number = 1

if number == 1:
    length = 3
    # length = float(input("Enter the length of the side of the square: "))
    area = length**2
    print("The area of the square is: ", area)
elif number == 2:
    base = 3
    # base = float(input("Enter the length of the base of the triangle: "))
    height = 7
    # height = float(input("Enter the height of the triangle: "))
    area = 1/2 * base * height
    print("The area of the triangle is: ", area)
else:
    print("Invalid input.")


# Ask the user to enter a number between 1 and 12 and then display the times table for that number.
print(" ")

number = 5
# number = int(input("Enter a number to display its timetable: "))
for i in range(1,number+1):
    for j in range(1,13):
        print(i," * ", j, " = ", i * j)
    print(" ")

print(" ")

# Ask the user to enter a number and then enter another number. Add these two numbers together and then ask if they want to add another number. If they enter “y", ask them to enter another number and keep adding numbers until they do not answer “y”. Once the loop has stopped, displaythe total.
print(" ")
number = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))
result = number + number2
print(number, " + ", number2, " = ", result)

another = input("Do you want to add another number? (y/n) ")
another = another.lower()
while another == "y":
    new_number = float(input("Enter another number: "))
    result = result + new_number
    print(result)
    another = input("Do you want to add another number? (y/n) ")
    another = another.lower()
print("Thanks for using my app.")


# Using the song “10 green bottles”, display the lines “There are [num] green bottles hanging on the wall, [num] green bottles hanging on the wall, and if 1 green bottle should accidentally fall”. Then ask the question “how many green bottles will be hanging on the wall?” If the user answers correctly, display the message “There will be [num] green bottles hanging on the wall”. If they answer incorrectly, display the message “No, try again” until they get it right. When the number of green bottles gets down to 0, display the message “There are no more green bottles hanging on the wall”. 

bottles = 10
while bottles >= 0:
    print("")
    print(bottles, "green bottles hanging on the wall.")
    question = int(input("If one green bottle should accidentaly fall, how many green bottles will be left hanging on the wall? "))
    bottles -= 1
    if bottles == question:
        print("There will be", bottles,"green bottles hanging on the wall.")
    else:
        while question != bottles:
            print("Wrong. Try again.")
            question = int(input("If one green bottle should accidentaly fall, how many green bottles will be left hanging on the wall? "))
print("No more bottles hanging on the wall.")