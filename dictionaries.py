dictionary = {"J-Nissi":2014, "BMJS":2020, "PAU":2024} # dictionary is made up of key value pairs
print(dictionary["J-Nissi"]) # acessing the value using the key

dictionary["Masters?"] = 2024 #including another key value pair
print(dictionary)

dictionary["random?"] = 1234 #including another key value pair
print(dictionary)

del(dictionary["random?"]) # delete a pair
print(dictionary)

print("BMJS" in dictionary) # check if a key is present... returns TRUE