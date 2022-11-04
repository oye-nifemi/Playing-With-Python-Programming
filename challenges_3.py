#  Ask the user to type in their name and then tell them how many vowels are in their name. 
name = input("Enter your name: ")
name = name.lower()
vowels = ["a","e","i","o","u"]
vow_num = 0

for i in name:
    if i in vowels:
        vow_num += 1
        
print("There are", vow_num,"vowels in your name.")



# Password authentication. Case sensitive
password = input("Enter your password: ")
password_confirm = input("Confirm your password: ")

if password == password_confirm:
    print("Thank you.")
elif password.lower() == password_confirm.lower():
    print("They must be the same case.")
else:
    print("Incorrect.")
    
    
    
# Ask the user for a list of five integers. Store them in an array. Sort the list and display it in reverse order. 
from array import *

integers = array('i', [])
for i in range(1, 6):
    entry = int(input("Enter an integer: "))
    integers.append(entry)
    
integers = sorted(integers)
integers.reverse()

print(integers)