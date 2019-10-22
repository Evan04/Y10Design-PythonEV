#Evan Van
#Upper Canada College
#Y10 Coding
#Mr. Jugoon

import json
import requests
import pprint

#––––––––––––––––––––––––––––––––––––––– Request –––––––––––––––––––––––––––––––––––––––

request = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t=Arsenal")

request_text = request.text

data = json.loads(request_text)

#––––––––––––––––––––––––––––––––––– List of Players –––––––––––––––––––––––––––––––––––

varPlayer = input("Which player do you want information on? \n 1. Hector Bellerin \n 2. Mesut Ozil \n 3. Emiliano Martinez \n 4. Calum Chambers \n 5. Matt Macey \n 6. Ainsley Maitland-Niles \n 7. Kieran Tierney \n 8. Alexandre Lacazette \n 9. Shkodran Mustafi \n 10. David Luiz \n 11. Sokratis Papastathopoulos \n 12. Pierre-Emerick Aubameyang \n 13. Bernd Leno \n 14. Daniel Ceballos \n 15. Granit Xhaka \n 16. Rob Holding \n 17. Sead Kolasinac \n 18. Konstantinos Mavropanos \n 19. Matteo Guendouzi \n 20. Lucas Torreira \n 21. Unai Emery \n 22. Nicolas Pepe \n 23. Jherson Vergara \n 24. Victor Alvarez \n 25. Maksim Belyayev \n")

#––––––––––––––––––––––––––––––––––– Hector Bellerin –––––––––––––––––––––––––––––––––––

if varPlayer == "1":
    print(" ")
    varOptions = input("Selected: Hector Bellerin \nChoose An Option About This Player \n 1. Date of Birth \n 2. Location of Birth \n 3. Position \n 4. Description \n")

    if varOptions == "1":
        varData = request.json()
        varChoice = varData ['player'][0]['dateBorn']
        print ("Date of Birth: " + varChoice)
    elif varOptions == "2":
        varData = request.json()
        varChoice = varData ['player'][0]['strNationality']
        print ("Location of Birth: " + varChoice)
    elif varOptions == "3":
        varData = request.json()
        varChoice = varData ['player'][0]['strPosition']
        print ("Position: " + varChoice)
    elif varOptions == "4":
        varData = request.json()
        varChoice = varData ['player'][0]['strDescriptionEN']
        print ("Description: " + varChoice)

    else:
        print("Invalid Number")
        print("Have A Nice Day!")

#––––––––––––––––––––––––––––––––––––– Mesut Ozil –––––––––––––––––––––––––––––––––––––

if varPlayer == "2":
    print(" ")
    varOptions = input("Selected: Mesut Ozil \nChoose An Option About This Player \n 1. Date of Birth \n 2. Location of Birth \n 3. Position \n 4. Description \n")

    if varOptions == "1":
        varData = request.json()
        varChoice = varData ['player'][1]['dateBorn']
        print ("Date of Birth: " + varChoice)
    elif varOptions == "2":
        varData = request.json()
        varChoice = varData ['player'][1]['strNationality']
        print ("Location of Birth: " + varChoice)
    elif varOptions == "3":
        varData = request.json()
        varChoice = varData ['player'][1]['strPosition']
        print ("Position: " + varChoice)
    elif varOptions == "4":
        varData = request.json()
        varChoice = varData ['player'][1]['strDescriptionEN']
        print ("Description: " + varChoice)

    else:
        print("Invalid Number")
        print("Have A Nice Day!")

#––––––––––––––––––––––––––––––––– Emiliano Martinez –––––––––––––––––––––––––––––––––

if varPlayer == "3":
    print(" ")
    varOptions = input("Selected: Emiliano Martinez \nChoose An Option About This Player \n 1. Date of Birth \n 2. Location of Birth \n 3. Position \n 4. Description \n")

    if varOptions == "1":
        varData = request.json()
        varChoice = varData ['player'][2]['dateBorn']
        print ("Date of Birth: " + varChoice)
    elif varOptions == "2":
        varData = request.json()
        varChoice = varData ['player'][2]['strNationality']
        print ("Location of Birth: " + varChoice)
    elif varOptions == "3":
        varData = request.json()
        varChoice = varData ['player'][2]['strPosition']
        print ("Position: " + varChoice)
    elif varOptions == "4":
        varData = request.json()
        varChoice = varData ['player'][2]['strDescriptionEN']
        print ("Description: " + varChoice)

    else:
        print("Invalid Number")
        print("Have A Nice Day!")

#–––––––––––––––––––––––––––––––––– Calum Chambers ––––––––––––––––––––––––––––––––––

if varPlayer == "4":
    print(" ")
    varOptions = input("Selected: Calum Chambers \nChoose An Option About This Player \n 1. Date of Birth \n 2. Location of Birth \n 3. Position \n 4. Description \n")

    if varOptions == "1":
        varData = request.json()
        varChoice = varData ['player'][3]['dateBorn']
        print ("Date of Birth: " + varChoice)
    elif varOptions == "2":
        varData = request.json()
        varChoice = varData ['player'][3]['strNationality']
        print ("Location of Birth: " + varChoice)
    elif varOptions == "3":
        varData = request.json()
        varChoice = varData ['player'][3]['strPosition']
        print ("Position: " + varChoice)
    elif varOptions == "4":
        varData = request.json()
        varChoice = varData ['player'][3]['strDescriptionEN']
        print ("Description: " + varChoice)

    else:
        print("Invalid Number")
        print("Have A Nice Day!")

#––––––––––––––––––––––––––––––––––– Matt Macey –––––––––––––––––––––––––––––––––––

if varPlayer == "5":
    print(" ")
    varOptions = input("Selected: Matt Macey \nChoose An Option About This Player \n 1. Date of Birth \n 2. Location of Birth \n 3. Position \n 4. Description \n")

    if varOptions == "1":
        varData = request.json()
        varChoice = varData ['player'][4]['dateBorn']
        print ("Date of Birth: " + varChoice)
    elif varOptions == "2":
        varData = request.json()
        varChoice = varData ['player'][4]['strNationality']
        print ("Location of Birth: " + varChoice)
    elif varOptions == "3":
        varData = request.json()
        varChoice = varData ['player'][4]['strPosition']
        print ("Position: " + varChoice)
    elif varOptions == "4":
        varData = request.json()
        varChoice = varData ['player'][4]['strDescriptionEN']
        print ("Description: " + varChoice)

    else:
        print("Invalid Number")
        print("Have A Nice Day!")

#––––––––––––––––––––––––––––– Ainsley Maitland-Niles –––––––––––––––––––––––––––––

if varPlayer == "6":
    print(" ")
    varOptions = input("Selected: Ainsley Maitland-Niles \nChoose An Option About This Player \n 1. Date of Birth \n 2. Location of Birth \n 3. Position \n 4. Description \n")

    if varOptions == "1":
        varData = request.json()
        varChoice = varData ['player'][5]['dateBorn']
        print ("Date of Birth: " + varChoice)
    elif varOptions == "2":
        varData = request.json()
        varChoice = varData ['player'][5]['strNationality']
        print ("Location of Birth: " + varChoice)
    elif varOptions == "3":
        varData = request.json()
        varChoice = varData ['player'][5]['strPosition']
        print ("Position: " + varChoice)
    elif varOptions == "4":
        varData = request.json()
        varChoice = varData ['player'][5]['strDescriptionEN']
        print ("Description: " + varChoice)

    else:
        print("Invalid Number")
        print("Have A Nice Day!")

#––––––––––––––––––––––––––––––––– Kieran Tierney ––––––––––––––––––––––––––––––––

if varPlayer == "7":
    print(" ")
    varOptions = input("Selected: Kieran Tierney \nChoose An Option About This Player \n 1. Date of Birth \n 2. Location of Birth \n 3. Position \n 4. Description \n")

    if varOptions == "1":
        varData = request.json()
        varChoice = varData ['player'][6]['dateBorn']
        print ("Date of Birth: " + varChoice)
    elif varOptions == "2":
        varData = request.json()
        varChoice = varData ['player'][6]['strNationality']
        print ("Location of Birth: " + varChoice)
    elif varOptions == "3":
        varData = request.json()
        varChoice = varData ['player'][6]['strPosition']
        print ("Position: " + varChoice)
    elif varOptions == "4":
        varData = request.json()
        varChoice = varData ['player'][6]['strDescriptionEN']
        print ("Description: " + varChoice)

    else:
        print("Invalid Number")
        print("Have A Nice Day!")

#–––––––––––––––––––––––––––––– Alexandre Lacazette ––––––––––––––––––––––––––––––

if varPlayer == "8":
    print(" ")
    varOptions = input("Selected: Alexandre Lacazette \nChoose An Option About This Player \n 1. Date of Birth \n 2. Location of Birth \n 3. Position \n 4. Description \n")

    if varOptions == "1":
        varData = request.json()
        varChoice = varData ['player'][7]['dateBorn']
        print ("Date of Birth: " + varChoice)
    elif varOptions == "2":
        varData = request.json()
        varChoice = varData ['player'][7]['strNationality']
        print ("Location of Birth: " + varChoice)
    elif varOptions == "3":
        varData = request.json()
        varChoice = varData ['player'][7]['strPosition']
        print ("Position: " + varChoice)
    elif varOptions == "4":
        varData = request.json()
        varChoice = varData ['player'][7]['strDescriptionEN']
        print ("Description: " + varChoice)

    else:
        print("Invalid Number")
        print("Have A Nice Day!")

#––––––––––––––––––––––––––––––– Shkodran Mustafi –––––––––––––––––––––––––––––––

if varPlayer == "9":
    print(" ")
    varOptions = input("Selected: Shkodran Mustafi \nChoose An Option About This Player \n 1. Date of Birth \n 2. Location of Birth \n 3. Position \n 4. Description \n")

    if varOptions == "1":
        varData = request.json()
        varChoice = varData ['player'][8]['dateBorn']
        print ("Date of Birth: " + varChoice)
    elif varOptions == "2":
        varData = request.json()
        varChoice = varData ['player'][8]['strNationality']
        print ("Location of Birth: " + varChoice)
    elif varOptions == "3":
        varData = request.json()
        varChoice = varData ['player'][8]['strPosition']
        print ("Position: " + varChoice)
    elif varOptions == "4":
        varData = request.json()
        varChoice = varData ['player'][8]['strDescriptionEN']
        print ("Description: " + varChoice)

    else:
        print("Invalid Number")
        print("Have A Nice Day!")

#–––––––––––––––––––––––––––––––––– David Luiz ––––––––––––––––––––––––––––––––––

if varPlayer == "10":
    print(" ")
    varOptions = input("Selected: David Luiz \nChoose An Option About This Player \n 1. Date of Birth \n 2. Location of Birth \n 3. Position \n 4. Description \n")

    if varOptions == "1":
        varData = request.json()
        varChoice = varData ['player'][9]['dateBorn']
        print ("Date of Birth: " + varChoice)
    elif varOptions == "2":
        varData = request.json()
        varChoice = varData ['player'][9]['strNationality']
        print ("Location of Birth: " + varChoice)
    elif varOptions == "3":
        varData = request.json()
        varChoice = varData ['player'][9]['strPosition']
        print ("Position: " + varChoice)
    elif varOptions == "4":
        varData = request.json()
        varChoice = varData ['player'][9]['strDescriptionEN']
        print ("Description: " + varChoice)

    else:
        print("Invalid Number")
        print("Have A Nice Day!")

#–––––––––––––––––––––––––– Sokratis Papastathopoulos ––––––––––––––––––––––––––

if varPlayer == "11":
    print(" ")
    varOptions = input("Selected: Sokratis Papastathopoulos \nChoose An Option About This Player \n 1. Date of Birth \n 2. Location of Birth \n 3. Position \n 4. Description \n")

    if varOptions == "1":
        varData = request.json()
        varChoice = varData ['player'][10]['dateBorn']
        print ("Date of Birth: " + varChoice)
    elif varOptions == "2":
        varData = request.json()
        varChoice = varData ['player'][10]['strNationality']
        print ("Location of Birth: " + varChoice)
    elif varOptions == "3":
        varData = request.json()
        varChoice = varData ['player'][10]['strPosition']
        print ("Position: " + varChoice)
    elif varOptions == "4":
        varData = request.json()
        varChoice = varData ['player'][10]['strDescriptionEN']
        print ("Description: " + varChoice)

    else:
        print("Invalid Number")
        print("Have A Nice Day!")

#–––––––––––––––––––––––––– Pierre-Emerick Aubameyang ––––––––––––––––––––––––––

if varPlayer == "12":
    print(" ")
    varOptions = input("Selected: Pierre-Emerick Aubameyang \nChoose An Option About This Player \n 1. Date of Birth \n 2. Location of Birth \n 3. Position \n 4. Description \n")

    if varOptions == "1":
        varData = request.json()
        varChoice = varData ['player'][11]['dateBorn']
        print ("Date of Birth: " + varChoice)
    elif varOptions == "2":
        varData = request.json()
        varChoice = varData ['player'][11]['strNationality']
        print ("Location of Birth: " + varChoice)
    elif varOptions == "3":
        varData = request.json()
        varChoice = varData ['player'][11]['strPosition']
        print ("Position: " + varChoice)
    elif varOptions == "4":
        varData = request.json()
        varChoice = varData ['player'][11]['strDescriptionEN']
        print ("Description: " + varChoice)

    else:
        print("Invalid Number")
        print("Have A Nice Day!")

#––––––––––––––––––––––––––––––––– Bernd Leno –––––––––––––––––––––––––––––––––

if varPlayer == "13":
    print(" ")
    varOptions = input("Selected: Bernd Leno \nChoose An Option About This Player \n 1. Date of Birth \n 2. Location of Birth \n 3. Position \n 4. Description \n")

    if varOptions == "1":
        varData = request.json()
        varChoice = varData ['player'][12]['dateBorn']
        print ("Date of Birth: " + varChoice)
    elif varOptions == "2":
        varData = request.json()
        varChoice = varData ['player'][12]['strNationality']
        print ("Location of Birth: " + varChoice)
    elif varOptions == "3":
        varData = request.json()
        varChoice = varData ['player'][12]['strPosition']
        print ("Position: " + varChoice)
    elif varOptions == "4":
        varData = request.json()
        varChoice = varData ['player'][12]['strDescriptionEN']
        print ("Description: " + varChoice)

    else:
        print("Invalid Number")
        print("Have A Nice Day!")

#–––––––––––––––––––––––––––––– Daniel Cebellos ––––––––––––––––––––––––––––––

if varPlayer == "14":
    print(" ")
    varOptions = input("Selected: Daniel Cebellos \nChoose An Option About This Player \n 1. Date of Birth \n 2. Location of Birth \n 3. Position \n 4. Description \n")

    if varOptions == "1":
        varData = request.json()
        varChoice = varData ['player'][13]['dateBorn']
        print ("Date of Birth: " + varChoice)
    elif varOptions == "2":
        varData = request.json()
        varChoice = varData ['player'][13]['strNationality']
        print ("Location of Birth: " + varChoice)
    elif varOptions == "3":
        varData = request.json()
        varChoice = varData ['player'][13]['strPosition']
        print ("Position: " + varChoice)
    elif varOptions == "4":
        varData = request.json()
        varChoice = varData ['player'][13]['strDescriptionEN']
        print ("Description: " + varChoice)

    else:
        print("Invalid Number")
        print("Have A Nice Day!")

#––––––––––––––––––––––––––––––– Granit Xhaka –––––––––––––––––––––––––––––––

if varPlayer == "15":
    print(" ")
    varOptions = input("Selected: Granit Xhaka \nChoose An Option About This Player \n 1. Date of Birth \n 2. Location of Birth \n 3. Position \n 4. Description \n")

    if varOptions == "1":
        varData = request.json()
        varChoice = varData ['player'][14]['dateBorn']
        print ("Date of Birth: " + varChoice)
    elif varOptions == "2":
        varData = request.json()
        varChoice = varData ['player'][14]['strNationality']
        print ("Location of Birth: " + varChoice)
    elif varOptions == "3":
        varData = request.json()
        varChoice = varData ['player'][14]['strPosition']
        print ("Position: " + varChoice)
    elif varOptions == "4":
        varData = request.json()
        varChoice = varData ['player'][14]['strDescriptionEN']
        print ("Description: " + varChoice)

    else:
        print("Invalid Number")
        print("Have A Nice Day!")

#––––––––––––––––––––––––––––––– Rob Holding –––––––––––––––––––––––––––––––

if varPlayer == "16":
    print(" ")
    varOptions = input("Selected: Rob Holding \nChoose An Option About This Player \n 1. Date of Birth \n 2. Location of Birth \n 3. Position \n 4. Description \n")

    if varOptions == "1":
        varData = request.json()
        varChoice = varData ['player'][15]['dateBorn']
        print ("Date of Birth: " + varChoice)
    elif varOptions == "2":
        varData = request.json()
        varChoice = varData ['player'][15]['strNationality']
        print ("Location of Birth: " + varChoice)
    elif varOptions == "3":
        varData = request.json()
        varChoice = varData ['player'][15]['strPosition']
        print ("Position: " + varChoice)
    elif varOptions == "4":
        varData = request.json()
        varChoice = varData ['player'][15]['strDescriptionEN']
        print ("Description: " + varChoice)

    else:
        print("Invalid Number")
        print("Have A Nice Day!")

#––––––––––––––––––––––––––––– Sead Kolasinac –––––––––––––––––––––––––––––

if varPlayer == "17":
    print(" ")
    varOptions = input("Selected: Sead Kolasinac \nChoose An Option About This Player \n 1. Date of Birth \n 2. Location of Birth \n 3. Position \n 4. Description \n")

    if varOptions == "1":
        varData = request.json()
        varChoice = varData ['player'][16]['dateBorn']
        print ("Date of Birth: " + varChoice)
    elif varOptions == "2":
        varData = request.json()
        varChoice = varData ['player'][16]['strNationality']
        print ("Location of Birth: " + varChoice)
    elif varOptions == "3":
        varData = request.json()
        varChoice = varData ['player'][16]['strPosition']
        print ("Position: " + varChoice)
    elif varOptions == "4":
        varData = request.json()
        varChoice = varData ['player'][16]['strDescriptionEN']
        print ("Description: " + varChoice)

    else:
        print("Invalid Number")
        print("Have A Nice Day!")

#–––––––––––––––––––––––– Konstantinos Mavropanos ––––––––––––––––––––––––

if varPlayer == "18":
    print(" ")
    varOptions = input("Selected: Konstantinos Mavropanos \nChoose An Option About This Player \n 1. Date of Birth \n 2. Location of Birth \n 3. Position \n 4. Description \n")

    if varOptions == "1":
        varData = request.json()
        varChoice = varData ['player'][17]['dateBorn']
        print ("Date of Birth: " + varChoice)
    elif varOptions == "2":
        varData = request.json()
        varChoice = varData ['player'][17]['strNationality']
        print ("Location of Birth: " + varChoice)
    elif varOptions == "3":
        varData = request.json()
        varChoice = varData ['player'][17]['strPosition']
        print ("Position: " + varChoice)
    elif varOptions == "4":
        varData = request.json()
        varChoice = varData ['player'][17]['strDescriptionEN']
        print ("Description: " + varChoice)

    else:
        print("Invalid Number")
        print("Have A Nice Day!")

#––––––––––––––––––––––––––– Matteo Guendouzi –––––––––––––––––––––––––––

if varPlayer == "19":
    print(" ")
    varOptions = input("Selected: Matteo Guendouzi \nChoose An Option About This Player \n 1. Date of Birth \n 2. Location of Birth \n 3. Position \n 4. Description \n")

    if varOptions == "1":
        varData = request.json()
        varChoice = varData ['player'][18]['dateBorn']
        print ("Date of Birth: " + varChoice)
    elif varOptions == "2":
        varData = request.json()
        varChoice = varData ['player'][18]['strNationality']
        print ("Location of Birth: " + varChoice)
    elif varOptions == "3":
        varData = request.json()
        varChoice = varData ['player'][18]['strPosition']
        print ("Position: " + varChoice)
    elif varOptions == "4":
        varData = request.json()
        varChoice = varData ['player'][18]['strDescriptionEN']
        print ("Description: " + varChoice)

    else:
        print("Invalid Number")
        print("Have A Nice Day!")

#–––––––––––––––––––––––––––– Lucas Torreira ––––––––––––––––––––––––––––

if varPlayer == "20":
    print(" ")
    varOptions = input("Selected: Lucas Torreira \nChoose An Option About This Player \n 1. Date of Birth \n 2. Location of Birth \n 3. Position \n 4. Description \n")

    if varOptions == "1":
        varData = request.json()
        varChoice = varData ['player'][19]['dateBorn']
        print ("Date of Birth: " + varChoice)
    elif varOptions == "2":
        varData = request.json()
        varChoice = varData ['player'][19]['strNationality']
        print ("Location of Birth: " + varChoice)
    elif varOptions == "3":
        varData = request.json()
        varChoice = varData ['player'][19]['strPosition']
        print ("Position: " + varChoice)
    elif varOptions == "4":
        varData = request.json()
        varChoice = varData ['player'][19]['strDescriptionEN']
        print ("Description: " + varChoice)

    else:
        print("Invalid Number")
        print("Have A Nice Day!")

#––––––––––––––––––––––––––––– Unai Emery –––––––––––––––––––––––––––––

if varPlayer == "21":
    print(" ")
    varOptions = input("Selected: Unai Emery \nChoose An Option About This Player \n 1. Date of Birth \n 2. Location of Birth \n 3. Position \n 4. Description \n")

    if varOptions == "1":
        varData = request.json()
        varChoice = varData ['player'][20]['dateBorn']
        print ("Date of Birth: " + varChoice)
    elif varOptions == "2":
        varData = request.json()
        varChoice = varData ['player'][20]['strNationality']
        print ("Location of Birth: " + varChoice)
    elif varOptions == "3":
        varData = request.json()
        varChoice = varData ['player'][20]['strPosition']
        print ("Position: " + varChoice)
    elif varOptions == "4":
        varData = request.json()
        varChoice = varData ['player'][20]['strDescriptionEN']
        print ("Description: " + varChoice)

    else:
        print("Invalid Number")
        print("Have A Nice Day!")

#–––––––––––––––––––––––––––– Nicolas Pepe ––––––––––––––––––––––––––––

if varPlayer == "22":
    print(" ")
    varOptions = input("Selected: Nicolas Pepe \nChoose An Option About This Player \n 1. Date of Birth \n 2. Location of Birth \n 3. Position \n 4. Description \n")

    if varOptions == "1":
        varData = request.json()
        varChoice = varData ['player'][21]['dateBorn']
        print ("Date of Birth: " + varChoice)
    elif varOptions == "2":
        varData = request.json()
        varChoice = varData ['player'][21]['strNationality']
        print ("Location of Birth: " + varChoice)
    elif varOptions == "3":
        varData = request.json()
        varChoice = varData ['player'][21]['strPosition']
        print ("Position: " + varChoice)
    elif varOptions == "4":
        varData = request.json()
        varChoice = varData ['player'][21]['strDescriptionEN']
        print ("Description: " + varChoice)

    else:
        print("Invalid Number")
        print("Have A Nice Day!")

#–––––––––––––––––––––––––– Jherson Vergara ––––––––––––––––––––––––––

if varPlayer == "23":
    print(" ")
    varOptions = input("Selected: Jherson Vergara \nChoose An Option About This Player \n 1. Date of Birth \n 2. Location of Birth \n 3. Position \n 4. Description \n")

    if varOptions == "1":
        varData = request.json()
        varChoice = varData ['player'][22]['dateBorn']
        print ("Date of Birth: " + varChoice)
    elif varOptions == "2":
        varData = request.json()
        varChoice = varData ['player'][22]['strNationality']
        print ("Location of Birth: " + varChoice)
    elif varOptions == "3":
        varData = request.json()
        varChoice = varData ['player'][22]['strPosition']
        print ("Position: " + varChoice)
    elif varOptions == "4":
        varData = request.json()
        varChoice = varData ['player'][22]['strDescriptionEN']
        print ("Description: " + varChoice)

    else:
        print("Invalid Number")
        print("Have A Nice Day!")

#–––––––––––––––––––––––––– Victor Alvarez ––––––––––––––––––––––––––

if varPlayer == "24":
    print(" ")
    varOptions = input("Selected: Victor Alvarez \nChoose An Option About This Player \n 1. Date of Birth \n 2. Location of Birth \n 3. Position \n 4. Description \n")

    if varOptions == "1":
        varData = request.json()
        varChoice = varData ['player'][23]['dateBorn']
        print ("Date of Birth: " + varChoice)
    elif varOptions == "2":
        varData = request.json()
        varChoice = varData ['player'][23]['strNationality']
        print ("Location of Birth: " + varChoice)
    elif varOptions == "3":
        varData = request.json()
        varChoice = varData ['player'][23]['strPosition']
        print ("Position: " + varChoice)
    elif varOptions == "4":
        varData = request.json()
        varChoice = varData ['player'][23]['strDescriptionEN']
        print ("Description: " + varChoice)

    else:
        print("Invalid Number")
        print("Have A Nice Day!")

#––––––––––––––––––––––––– Maksim Belyayev –––––––––––––––––––––––––

if varPlayer == "25":
    print(" ")
    varOptions = input("Selected: Maksim Belyayev \nChoose An Option About This Player \n 1. Date of Birth \n 2. Location of Birth \n 3. Position \n 4. Description \n")

    if varOptions == "1":
        varData = request.json()
        varChoice = varData ['player'][24]['dateBorn']
        print ("Date of Birth: " + varChoice)
    elif varOptions == "2":
        varData = request.json()
        varChoice = varData ['player'][24]['strNationality']
        print ("Location of Birth: " + varChoice)
    elif varOptions == "3":
        varData = request.json()
        varChoice = varData ['player'][24]['strPosition']
        print ("Position: " + varChoice)
    elif varOptions == "4":
        varData = request.json()
        varChoice = varData ['player'][24]['strDescriptionEN']
        print ("Description: " + varChoice)

    else:
        print("Invalid Number")
        print("Have A Nice Day!")

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

input("Press ENTER to quit the program")