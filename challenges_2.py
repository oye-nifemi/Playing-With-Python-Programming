# Make a maths quiz that asks five questions by randomly generating two whole numbers to make the question (e.g. [num1] + [num2]). Ask the user to enter the answer. If they get it right add a point to their score. At the end of the quiz, tell them how many they got correct out of five. 

import random
score = 0

for i in range(1,6):
    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, 100)
    print(number_1 ," + ", number_2, " = ", end="")
    entry = int(input())
    answer = number_1 + number_2
    if answer == entry:
        score = score + 1
print("You got ", score, "out of 5")


# Display five colours and ask the user to pick one. If they pick the same as the program has chosen, say “Well done”, otherwise display a witty answer which involves the correct colour, e.g. “I bet you are GREEN with envy” or “You are probably feeling BLUE right now”. Ask them to guess again; if they have still not got it right, keep giving them the same clue and ask the user to enter a colour until they guess it correctly. 

colors = ["red", "green", "blue", "pink", "brown"]
color = random.choice(colors)
print(color)
print("Guess the color: ", end="")
entry = input()
statement_1 = "I bet you are", color,"with envy"
statement_2 = "You are probably feeling", color,"right now"
statements = [statement_1, statement_2]
choose_statement = random.choice(statements)
if entry == color:
    print("Well done!")
else:
    while entry != color:
        print(choose_statement)
        entry = input()
print(str(statement_1))



import turtle

turtle.shape("turtle")
for i in range(0,360):
    turtle.forward(3)
    turtle.right(1)
turtle.exitonclick()


# Create a list containing four colors and display them on separate lines. Ask the user to enter another show and a position they want it inserted into the list. Display the list again, showing all five colors in their new positions.
list = ["red", "blue", "purple", "pink"]
print(list)
print("")

new_color = input("Enter a new color: ")
new_position = int(input("Enter the position that you wnat to insert this new color: "))

list.insert(new_position, new_color)
print(list)
print("")

for i in list:
    print(i)
print("")




#Create an empty list called “nums”. Ask the user to enter numbers. After each number is entered, add it to the end of the nums list and display the list. Once they have entered three numbers, ask them if they still want the last number they entered saved. If they say “no”, remove the last item from the list. Display the list of numbers.

nums = []
count = 0
for i in range(3):
    entry = input("Enter a number: ")
    nums.append(entry)
    count += 1
    if count == 3:
        delete = input("Do you want to delete the last number you entered? (y/n) : ")
        delete = delete[0]
        delete = delete.lower()
        if delete == "y":
            nums.remove(nums[-1])
            print(nums)
        else:
            print(nums)

    
# Ask the user to enter their first name and then display the length of their first name. Then ask for their surname and display the length of their surname. Join their first name and surname together with a space between and display the result. Finally, display the length of their full name (including the space). 

firstname = input("Enter your firstname: ")
print("The length of your firstname is: ", len(firstname))
lastname = input("Enter your lastname: ")
print("The length of your lastname is: ", len(lastname))
fullname = firstname + " " + lastname
print("Your fullname is: ", fullname)
print("The length of your fullname is: ", len(fullname))



# Ask the user to type in their favourite school subject. Display it with “-” after each letter, e.g. S-p-a-n-i-s-h-.
fav_sub = input("Enter your favourite school subject: ")
for i in fav_sub:
    print(i, end="-")




#Ask the user to type in a word and then display it backwards on separate lines.
word = input("Enter a word: ")
index = 1
for i in word:
    print(word[-1*index])
    index += 1
    