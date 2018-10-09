#A loop is a progrmamming structure that can repeat 
#a section of code.
#A loop can run the same code exactly over and over 
#again or with some thought it can generate a pattern.

#There are two broad catagories of loops
# Conditional Loops(while): These loops run as long as a condition is true

# Counted Loops(for): These loops using a counter to keep 
#track of how many times the loop has run

#You can use any loop in any situation, but usually from
#a design perspective there is a better loop in terms
#of coding.

#If you know in advance how many times a loop should
#run a COUNTED LOOP is usually the better choice

#If you don't know how many times a loop should run
#a CONDITIONAL LOOP is usually the better choice

print("************************************")
#taking inputs

#A while loop evaluates a condition when it is first reached
#If the condition is true it enters the loop block


word = "" #We have to delcare and initialize word so it fails the while loop
while len(word) < 6 or word.isalpha() == False:
	#Loop block

	word = input("Please input a word larger than 5 letters: ")
	if (len(word) < 6):
		print("Pleas input a word larger than 5 letters!")

	if(word.isalpha() == False):
		print("I said a real word")

	#When we reach the bottom of the loop block we check
	#the condition again. If it is true, we go back to 
	#the top of the block and run it again.

print(word+" is a seriously long word!")
#CAUTION: DO NOT USE LOOPS TO CONTROL INPUTS WITH GUI PROGRAMS










