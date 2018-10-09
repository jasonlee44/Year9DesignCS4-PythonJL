string = input("Please enter a string: ")


for i in range (0,len(string),1):
	if(string.isalpha() == False):
		print("Please enter a real string")
		break
	print(string[i]) #prints out each letter of string one by one








