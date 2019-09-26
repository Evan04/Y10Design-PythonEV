#Vending Machine
#Evan Van
#Upper Canada College

print(" ")
print("		     Welcome To The Vending Machine! ~(˘▾˘~)")
print(" ")
print("1. Milk - $2.25")
print(" ")
print("2. Apple - $1.25")
print(" ")
print("3. Bottled Water - $1.55")
print(" ")
print("4. Chicken Wings - $5.75")
print(" ")

#********************** Variables **********************

varItem = int(input("Please make your selection. \n"))

varMoney = 0

varLost = 0

varPrice1 = 2.25

varPrice2 = 1.25

varPrice3 = 1.55

varPrice4 = 5.75

#*********************** Item #1 ***********************

if varItem == 1:
	varMoney = float(input("Selected: Milk. Please insert $2.25. \n"))

	if varMoney == 2.25:
		print("Here Is Your Milk.")
		print(" ")
		print("Hope It's Not Expired! ♪~ ᕕ(ᐛ)ᕗ")

	elif varMoney < 2.25:
		print("Insufficient Funds.")
		print(" ")
		print("Your Purchase Has Been Canceled And You Have Lost $"+str(varMoney)+". ༼ つ ಥ_ಥ ༽つ")

	elif varMoney > 2.25:

		varLost = varMoney - 2.25

		print("You have lost $"+str(varLost)+" since the milk only costed $"+str(varPrice1)+".")
		print(" ")
		print("Have A Fantastic Day! ლ(´ڡ`ლ)")

#*********************** Item #2 ***********************

elif varItem == 2:
	varMoney = float(input("Selected: Apple. Please insert $1.25. \n"))

	if varMoney == 1.25:
		print("Here Is Your Apple.")
		print(" ")
		print("Hope It's Not Rotten! ༼ つ ◕_◕ ༽つ")

	elif varMoney < 1.25:
		print("Insufficient Funds.")
		print(" ")
		print("Your Purchase Has Been Canceled And You Have Lost $"+str(varMoney)+". ╚(ಠ_ಠ)=┐")

	elif varMoney > 1.25:

		varLost = varMoney - 1.25

		print("You have lost $"+str(varLost)+" since the apple only costed $"+str(varPrice2)+".")
		print(" ")
		print("Have A Fantastic Day! (▰˘◡˘▰)")

#*********************** Item #3 ***********************

elif varItem == 3:
	varMoney = float(input("Selected: Bottled Water. Please insert $1.55. \n"))

	if varMoney == 1.55:
		print("Here Is Your Bottled Water.")
		print(" ")
		print("Hope It's Not Contaminated! ¯\_(ツ)_/¯") 

	elif varMoney < 1.55:
		print("Insufficient Funds.")
		print(" ")
		print("Your Purchase Has Been Canceled And You Have Lost $"+str(varMoney)+". ( ͡° ͜ʖ ͡°)")

	elif varMoney > 1.55:

		varLost = varMoney - 1.55

		print("You have lost $"+str(varLost)+" since the bottled water only costed $"+str(varPrice3)+".")
		print(" ")
		print("Have A Fantastic Day! (ง°ل͜°)ง")

#*********************** Item #4 ***********************

elif varItem == 4:
	varMoney = float(input("Selected: Chicken Wings. Please insert $5.75. \n"))

	if varMoney == 5.75:
		print("Here Are Your Chicken Wings.")
		print(" ")
		print("Hope It's Fully Cooked! (づ￣ ³￣)づ")

	elif varMoney < 5.75:
		print("Insufficient Funds.")
		print(" ")
		print("Your Purchase Has Been Canceled And You Have Lost $"+str(varMoney)+". ʕ•ᴥ•ʔ")

	elif varMoney > 5.75:

		varLost = varMoney - 5.75

		print("You have lost $"+str(varLost)+" since the chicken wings only costed $"+str(varPrice4)+".")
		print(" ")
		print("Have A Fantastic Day! ᕙ(⇀‸↼‶)ᕗ")

input("Press ENTER to quit the program")