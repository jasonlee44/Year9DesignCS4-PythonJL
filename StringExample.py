#This file will go through the basics of string manipulation 

#Strings are collections of characters
#Strings are enclosed in "  " or ' '
# "Paul"
# "Paul is cool"
# "Paul is cool!"
#Two things we need to talk about when we think of strings
#index - Always starts at 0
#length

#Example
#0123	012345
# "Paul"	"Monkey"
# len("Paul") = 4
# len("Monkey") = 6

name = "Paul"

print(name) #I can print strings

sentence = name + " is cool!"
print(sentence)
print(sentence + "!")

#I can access specific letters
firstLetter = name[0]
print(firstLetter)
letters1 = name[0:2] #inclusive:exclusive
print(letters1)
letters2 = name[2:] # "ul"
print(letters2)

letters2a = name[2:len(name)]
print(letters2a)

letters3 = name[:2] # "Pa"
print(letters3)

lname = len(name)
print(lname)

#If I want to print out all letters
for i in range(len(name)):
	print(name[i])

