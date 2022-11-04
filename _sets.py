set_1 = {"a", "b", "c", "d", "a"}
set_2 = {"1", "2", "3", "d", "a"}
set_3 = {"1", "2", "3"}

print(set_1)

set_1.add("123456") # add new element to set_1
print(set_1)

set_1.remove("123456") # remove new element from set_1
print(set_1)

print("a" in set_1)

print(set_1 & set_2) # print elements common to both sets

print(set_3.issubset(set_2)) #check if set_3 is a subset of set_2

print(set_1.difference(set_2)) # Find the difference in set1 but not set2

print(set_2.difference(set_1)) # Find the difference in set_2 but not set_1