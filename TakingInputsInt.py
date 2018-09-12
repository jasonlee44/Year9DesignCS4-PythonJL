#Input
#Assignment Statement
r = input("What is the radius: ")
r = int(r) #changes the input into an integer 

h = int(input("What is the height: "))

#Process
ans = 2*3.14*r*r + 2*r*h*3.14

#Output
printLine(ans)
