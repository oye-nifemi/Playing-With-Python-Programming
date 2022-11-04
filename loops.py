# the range function
print(tuple(range(3)))
print(list(range(3)))
print(set(range(3)))

# loops
squares = ["red", "yellow", "blue", "green", "purple"]
for square in range(0,5):
    squares[square] = "white"
    
print(squares)

# while loop
list_1 = ["red","red","orange","red","red","purple"]
list_2 = []
print(list_2)

i=0

while list_1[i] == "red":
    list_2.append(list_1[i])
    i += 1
print(list_2)




squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i=0
while(squares[i]=="orange"):
    new_squares.append(squares[i])
    i+=1
    
print(new_squares)