print("1. What is your favorite subject in school?")
print("2. What is your favorite colour?")
print("3. How many siblings do you have?")
print(" ")
print("Choose one of the options above")

myrequest = int(input("Tell me what you would like to know \n"))

if myrequest == 1:
	print("Answer: Chemistry")
elif myrequest == 2:
	print("Answer: Blue")
elif myrequest == 3:
	print("Answer: 2 siblings")
else:
	print("That was not a valid choice silly.")