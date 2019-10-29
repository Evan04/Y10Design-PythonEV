#Evan Van
#Upper Canada College
#Y10 Design - Coding
#Mr. Jugoon

import json
import requests
import webbrowser

#–––––––––––––––––––––––––––––––– Helper Functions –––––––––––––––––––––––––––––––

#The datas below act as "place holders"
def writeHTML(data1, data2, data3, data4, data5):
    myfile = open("playerAPI.html","w")

    #The file's location is different for every user
    filename1 = 'file:///Users/evan.van/Desktop//Git Repo/Y10Design-PythonEV/playerAPI.html'

    #Opens the HTML file in a new tab
    webbrowser.open_new_tab(filename1)
    
#–––––––––––––––––––––––––––––––––––– HTML/CSS –––––––––––––––––––––––––––––––––––
   
    #The HTML code for the webpage
    myfile.write("""
<!DOCTYPE html>
<html>

    <title>Arsenal F.C. Player Info</title>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    body, html {
      height: 100%;
      margin: 0;
      font: 400 15px/1.8 "Lato", sans-serif;
      color: #db3535;
    }

    .image1, .image2 {
      position: relative;
      opacity: 0.65;
      background-attachment: fixed;
      background-position: center;
      background-repeat: no-repeat;
      background-size: cover;

    }
    .image1 {
      background-image: url("https://images7.alphacoders.com/970/970081.jpg");
      min-height: 100%;
    }

    .image2 {
      background-image: url("https://premierleague-static-files.s3.amazonaws.com/premierleague/photo/2017/11/30/7e5cfb87-c1b8-49c3-9a5a-c8fb84d94ab8/882108058.jpg");
      min-height: 750px;
    }

    .caption {
      position: absolute;
      left: 0;
      top: 50%;
      width: 100%;
      text-align: center;
      color: #000;
    }

    .caption span.border {
      background-color: #111;
      color: #fff;
      padding: 18px;
      font-size: 25px;
      letter-spacing: 10px;
    }

    h1 {
      letter-spacing: 5px;
      text-transform: uppercase;
      font: 20px "Lato", sans-serif;
      color: #111;
    }

    }
    </style>
    </head>
    <body>

    <div class="image1">
      <div class="caption">
      <span class="border">"""+ data1+"""</span>
      </div>
    </div>

    <div style="color: #777;background-color:white;text-align:center;padding:75px 200px;text-align: justify;">
      <h1 style="text-align:center;">Player Information</h1>
      <p>Date of Birth: """+ data2+"""</p>
      <p>Position: """+ data3+"""</p>
      <p>Nationality: """+ data4+"""</p>
      <p>Description: """+ data5+"""</p>

    </div>

    <div class="image2">
      <div class="caption">
      <span class="border">Go to <a href='https://www.thesportsdb.com/api.php'>The Sports DB</a> for API Info</span>
      </div>
    </div>


    </body></html>""")

    myfile.close()

#––––––––––––––––––––––––––––––––––––––– Request –––––––––––––––––––––––––––––––––––––––

#Contains the data retrieved by "requests" from the api site
request = requests.get("https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t=Arsenal")

request_text = request.text

data = json.loads(request_text)

#––––––––––––––––––––––––––––––––––– List of Players –––––––––––––––––––––––––––––––––––

#Displays the players on the Arsenal F.C. Team
varPlayer = input("List of Arsenal F.C. Players \nPlease Select A Player \n 1. Hector Bellerin \n 2. Mesut Ozil \n 3. Emiliano Martinez \n 4. Calum Chambers \n 5. Matt Macey \n 6. Ainsley Maitland-Niles \n 7. Kieran Tierney \n 8. Alexandre Lacazette \n 9. Shkodran Mustafi \n 10. David Luiz \n 11. Sokratis Papastathopoulos \n 12. Pierre-Emerick Aubameyang \n 13. Bernd Leno \n 14. Daniel Ceballos \n 15. Granit Xhaka \n 16. Rob Holding \n 17. Sead Kolasinac \n 18. Konstantinos Mavropanos \n 19. Matteo Guendouzi \n 20. Lucas Torreira \n 21. Unai Emery \n 22. Nicolas Pepe \n 23. Jherson Vergara \n 24. Victor Alvarez \n 25. Maksim Belyayev \n")

#––––––––––––––––––––––––––––––––––– Hector Bellerin –––––––––––––––––––––––––––––––––––

#The following code below is repeated 25 times for each player
#Displays the selected player when the user enters "1"
if varPlayer == "1":
    print(" ")
    print ("Selected Player: Hector Bellerin")

    #Pulls specific data from the API (ie. player name, player position, etc)
    varData = request.json()
    varPlayer1 = varData ['player'] [0] ['strPlayer']
    varBorn1 = varData ['player'][0]['dateBorn']
    varPosition1 = varData ['player'][0]['strPosition']
    varNationality1 = varData ['player'][0]['strNationality']
    varDescription1 = varData ['player'][0]['strDescriptionEN']

    #Allows the user to either enter "y" for yes and "n" for no    
    openWeb = input("Would you like to open this information in a webpage? y/n \n")

    #The user can either enter a capital or lowercase "y"
    if openWeb == "y":
        
        #These variables are used in the HTML section above
        writeHTML(varPlayer1, varBorn1, varPosition1, varNationality1, varDescription1)

    #The user can either enter a capital or lowercase "n"
    elif openWeb == "n":

        print(" ")
        print("Thank you for using this program")
        print(" ")

        #A graceful way to exit the program
        input("Press ENTER to quit the program")

    #If the user types anything else besides a "y" or "n", then the program would display that the character is invalid
    else:

        print(" ")
        print("Invalid Character Given")
        print(" ")
        input("Press ENTER to quit the program")


#––––––––––––––––––––––––––––––––––––– Mesut Ozil –––––––––––––––––––––––––––––––––––––

elif varPlayer == "2":
    print(" ")
    print ("Selected Player: Mesut Ozil")

    varData = request.json()
    varPlayer2 = varData ['player'] [1] ['strPlayer']
    varBorn2 = varData ['player'][1]['dateBorn']
    varPosition2 = varData ['player'][1]['strPosition']
    varNationality2 = varData ['player'][1]['strNationality']
    varDescription2 = varData ['player'][1]['strDescriptionEN']
        
    openWeb = input("Would you like to open this information in a webpage? y/n \n")

    if openWeb == "y":
            
        writeHTML(varPlayer2, varBorn2, varPosition2, varNationality2, varDescription2)

    elif openWeb == "n":

        print(" ")
        print("Thank you for using this program")
        print(" ")
        input("Press ENTER to quit the program")

    else:

        print(" ")
        print("Invalid Character Given")
        print(" ")
        input("Press ENTER to quit the program")

#––––––––––––––––––––––––––––––––– Emiliano Martinez –––––––––––––––––––––––––––––––––

elif varPlayer == "3":
    print(" ")
    print ("Selected Player: Emiliano Martinez")

    varData = request.json()
    varPlayer3 = varData ['player'] [2] ['strPlayer']
    varBorn3 = varData ['player'][2]['dateBorn']
    varPosition3 = varData ['player'][2]['strPosition']
    varNationality3 = varData ['player'][2]['strNationality']
    varDescription3 = varData ['player'][2]['strDescriptionEN']
        
    openWeb = input("Would you like to open this information in a webpage? y/n \n")

    if openWeb == "y":
            
        writeHTML(varPlayer3, varBorn3, varPosition3, varNationality3, varDescription3)

    elif openWeb == "n":

        print(" ")
        print("Thank you for using this program")
        print(" ")
        input("Press ENTER to quit the program")

    else:

        print(" ")
        print("Invalid Character Given")
        print(" ")
        input("Press ENTER to quit the program")

#–––––––––––––––––––––––––––––––––– Calum Chambers ––––––––––––––––––––––––––––––––––

elif varPlayer == "4":
    print(" ")
    print ("Selected Player: Calum Chambers")

    varData = request.json()
    varPlayer4 = varData ['player'] [3] ['strPlayer']
    varBorn4 = varData ['player'][3]['dateBorn']
    varPosition4 = varData ['player'][3]['strPosition']
    varNationality4 = varData ['player'][3]['strNationality']
    varDescription4 = varData ['player'][3]['strDescriptionEN']
        
    openWeb = input("Would you like to open this information in a webpage? y/n \n")

    if openWeb == "y":
            
        writeHTML(varPlayer4, varBorn4, varPosition4, varNationality4, varDescription4)

    elif openWeb == "n":

        print(" ")
        print("Thank you for using this program")
        print(" ")
        input("Press ENTER to quit the program")

    else:

        print(" ")
        print("Invalid Character Given")
        print(" ")
        input("Press ENTER to quit the program")

#––––––––––––––––––––––––––––––––––– Matt Macey –––––––––––––––––––––––––––––––––––

elif varPlayer == "5":
    print(" ")
    print ("Selected Player: Matt Macey")

    varData = request.json()
    varPlayer5 = varData ['player'] [4] ['strPlayer']
    varBorn5 = varData ['player'][4]['dateBorn']
    varPosition5 = varData ['player'][4]['strPosition']
    varNationality5 = varData ['player'][4]['strNationality']
    varDescription5 = varData ['player'][4]['strDescriptionEN']
        
    openWeb = input("Would you like to open this information in a webpage? y/n \n")

    if openWeb == "y":
            
        writeHTML(varPlayer5, varBorn5, varPosition5, varNationality5, varDescription5)

    elif openWeb == "n":

        print(" ")
        print("Thank you for using this program")
        print(" ")
        input("Press ENTER to quit the program")

    else:

        print(" ")
        print("Invalid Character Given")
        print(" ")
        input("Press ENTER to quit the program")

#––––––––––––––––––––––––––––– Ainsley Maitland-Niles –––––––––––––––––––––––––––––

elif varPlayer == "6":
    print(" ")
    print ("Selected Player: Ainsley Maitland-Niles")

    varData = request.json()
    varPlayer6 = varData ['player'] [5] ['strPlayer']
    varBorn6 = varData ['player'][5]['dateBorn']
    varPosition6 = varData ['player'][5]['strPosition']
    varNationality6 = varData ['player'][5]['strNationality']
    varDescription6 = varData ['player'][5]['strDescriptionEN']
        
    openWeb = input("Would you like to open this information in a webpage? y/n \n")

    if openWeb == "y":
            
        writeHTML(varPlayer6, varBorn6, varPosition6, varNationality6, varDescription6)

    elif openWeb == "n":

        print(" ")
        print("Thank you for using this program")
        print(" ")
        input("Press ENTER to quit the program")

    else:

        print(" ")
        print("Invalid Character Given")
        print(" ")
        input("Press ENTER to quit the program")

#––––––––––––––––––––––––––––––––– Kieran Tierney ––––––––––––––––––––––––––––––––

elif varPlayer == "7":
    print(" ")
    print ("Selected Player: Kieran Tierney")

    varData = request.json()
    varPlayer7 = varData ['player'] [6] ['strPlayer']
    varBorn7 = varData ['player'][6]['dateBorn']
    varPosition7 = varData ['player'][6]['strPosition']
    varNationality7 = varData ['player'][6]['strNationality']
    varDescription7 = varData ['player'][6]['strDescriptionEN']
        
    openWeb = input("Would you like to open this information in a webpage? y/n \n")

    if openWeb == "y":
            
        writeHTML(varPlayer7, varBorn7, varPosition7, varNationality7, varDescription7)

    elif openWeb == "n":

        print(" ")
        print("Thank you for using this program")
        print(" ")
        input("Press ENTER to quit the program")

    else:

        print(" ")
        print("Invalid Character Given")
        print(" ")
        input("Press ENTER to quit the program")

#–––––––––––––––––––––––––––––– Alexandre Lacazette ––––––––––––––––––––––––––––––

elif varPlayer == "8":
    print(" ")
    print ("Selected Player: Alexandre Lacazette")

    varData = request.json()
    varPlayer8 = varData ['player'] [7] ['strPlayer']
    varBorn8 = varData ['player'][7]['dateBorn']
    varPosition8 = varData ['player'][7]['strPosition']
    varNationality8 = varData ['player'][7]['strNationality']
    varDescription8 = varData ['player'][7]['strDescriptionEN']
        
    openWeb = input("Would you like to open this information in a webpage? y/n \n")

    if openWeb == "y":
            
        writeHTML(varPlayer8, varBorn8, varPosition8, varNationality8, varDescription8)

    elif openWeb == "n":

        print(" ")
        print("Thank you for using this program")
        print(" ")
        input("Press ENTER to quit the program")

    else:

        print(" ")
        print("Invalid Character Given")
        print(" ")
        input("Press ENTER to quit the program")

#––––––––––––––––––––––––––––––– Shkodran Mustafi –––––––––––––––––––––––––––––––

elif varPlayer == "9":
    print(" ")
    print ("Selected Player: Shkodran Mustafi")

    varData = request.json()
    varPlayer9 = varData ['player'] [8] ['strPlayer']
    varBorn9 = varData ['player'][8]['dateBorn']
    varPosition9 = varData ['player'][8]['strPosition']
    varNationality9 = varData ['player'][8]['strNationality']
    varDescription9 = varData ['player'][8]['strDescriptionEN']
        
    openWeb = input("Would you like to open this information in a webpage? y/n \n")

    if openWeb == "y":
            
        writeHTML(varPlayer9, varBorn9, varPosition9, varNationality9, varDescription9)

    elif openWeb == "n":

        print(" ")
        print("Thank you for using this program")
        print(" ")
        input("Press ENTER to quit the program")

    else:

        print(" ")
        print("Invalid Character Given")
        print(" ")
        input("Press ENTER to quit the program")

#–––––––––––––––––––––––––––––––––– David Luiz ––––––––––––––––––––––––––––––––––

elif varPlayer == "10":
    print(" ")
    print ("Selected Player: David Luiz")

    varData = request.json()
    varPlayer10 = varData ['player'] [9] ['strPlayer']
    varBorn10 = varData ['player'][9]['dateBorn']
    varPosition10 = varData ['player'][9]['strPosition']
    varNationality10 = varData ['player'][9]['strNationality']
    varDescription10 = varData ['player'][9]['strDescriptionEN']
        
    openWeb = input("Would you like to open this information in a webpage? y/n \n")

    if openWeb == "y":
            
        writeHTML(varPlayer10, varBorn10, varPosition10, varNationality10, varDescription10)

    elif openWeb == "n":

        print(" ")
        print("Thank you for using this program")
        print(" ")
        input("Press ENTER to quit the program")

    else:

        print(" ")
        print("Invalid Character Given")
        print(" ")
        input("Press ENTER to quit the program")

#–––––––––––––––––––––––––– Sokratis Papastathopoulos ––––––––––––––––––––––––––

if varPlayer == "11":
    print(" ")
    print ("Selected Player: Sokratis Papastathopoulos")

    varData = request.json()
    varPlayer11 = varData ['player'] [10] ['strPlayer']
    varBorn11 = varData ['player'][10]['dateBorn']
    varPosition11 = varData ['player'][10]['strPosition']
    varNationality11 = varData ['player'][10]['strNationality']
    varDescription11 = varData ['player'][10]['strDescriptionEN']
        
    openWeb = input("Would you like to open this information in a webpage? y/n \n")

    if openWeb == "y":
            
        writeHTML(varPlayer11, varBorn11, varPosition11, varNationality11, varDescription11)

    elif openWeb == "n":

        print(" ")
        print("Thank you for using this program")
        print(" ")
        input("Press ENTER to quit the program")

    else:

        print(" ")
        print("Invalid Character Given")
        print(" ")
        input("Press ENTER to quit the program")

#–––––––––––––––––––––––––– Pierre-Emerick Aubameyang ––––––––––––––––––––––––––

elif varPlayer == "12":
    print(" ")
    print ("Selected Player: Pierre-Emerick Aubameyang")

    varData = request.json()
    varPlayer12 = varData ['player'] [11] ['strPlayer']
    varBorn12 = varData ['player'][11]['dateBorn']
    varPosition12 = varData ['player'][11]['strPosition']
    varNationality12 = varData ['player'][11]['strNationality']
    varDescription12 = varData ['player'][11]['strDescriptionEN']
        
    openWeb = input("Would you like to open this information in a webpage? y/n \n")

    if openWeb == "y":
            
        writeHTML(varPlayer12, varBorn12, varPosition12, varNationality12, varDescription12)

    elif openWeb == "n":

        print(" ")
        print("Thank you for using this program")
        print(" ")
        input("Press ENTER to quit the program")

    else:

        print(" ")
        print("Invalid Character Given")
        print(" ")
        input("Press ENTER to quit the program")

#––––––––––––––––––––––––––––––––– Bernd Leno –––––––––––––––––––––––––––––––––

elif varPlayer == "13":
    print(" ")
    print ("Selected Player: Bernd Leno")

    varData = request.json()
    varPlayer13 = varData ['player'] [12] ['strPlayer']
    varBorn13 = varData ['player'][12]['dateBorn']
    varPosition13 = varData ['player'][12]['strPosition']
    varNationality13 = varData ['player'][12]['strNationality']
    varDescription13 = varData ['player'][12]['strDescriptionEN']
        
    openWeb = input("Would you like to open this information in a webpage? y/n \n")

    if openWeb == "y":
            
        writeHTML(varPlayer13, varBorn13, varPosition13, varNationality13, varDescription13)

    elif openWeb == "n":

        print(" ")
        print("Thank you for using this program")
        print(" ")
        input("Press ENTER to quit the program")

    else:

        print(" ")
        print("Invalid Character Given")
        print(" ")
        input("Press ENTER to quit the program")

#–––––––––––––––––––––––––––––– Daniel Ceballos ––––––––––––––––––––––––––––––

elif varPlayer == "14":
    print(" ")
    print ("Selected Player: Daniel Ceballos")

    varData = request.json()
    varPlayer14 = varData ['player'] [13] ['strPlayer']
    varBorn14 = varData ['player'][13]['dateBorn']
    varPosition14 = varData ['player'][13]['strPosition']
    varNationality14 = varData ['player'][13]['strNationality']
    varDescription14 = varData ['player'][13]['strDescriptionEN']
        
    openWeb = input("Would you like to open this information in a webpage? y/n \n")

    if openWeb == "y":
            
        writeHTML(varPlayer14, varBorn14, varPosition14, varNationality14, varDescription14)

    elif openWeb == "n":

        print(" ")
        print("Thank you for using this program")
        print(" ")
        input("Press ENTER to quit the program")

    else:

        print(" ")
        print("Invalid Character Given")
        print(" ")
        input("Press ENTER to quit the program")

#––––––––––––––––––––––––––––––– Granit Xhaka –––––––––––––––––––––––––––––––

elif varPlayer == "15":
    print(" ")
    print ("Selected Player: Granit Xhaka")

    varData = request.json()
    varPlayer15 = varData ['player'] [14] ['strPlayer']
    varBorn15 = varData ['player'][14]['dateBorn']
    varPosition15 = varData ['player'][14]['strPosition']
    varNationality15 = varData ['player'][14]['strNationality']
    varDescription15 = varData ['player'][14]['strDescriptionEN']
        
    openWeb = input("Would you like to open this information in a webpage? y/n \n")

    if openWeb == "y":
            
        writeHTML(varPlayer15, varBorn15, varPosition15, varNationality15, varDescription15)

    elif openWeb == "n":

        print(" ")
        print("Thank you for using this program")
        print(" ")
        input("Press ENTER to quit the program")

    else:

        print(" ")
        print("Invalid Character Given")
        print(" ")
        input("Press ENTER to quit the program")

#––––––––––––––––––––––––––––––– Rob Holding –––––––––––––––––––––––––––––––

elif varPlayer == "16":
    print(" ")
    print ("Selected Player: Rob Holding")

    varData = request.json()
    varPlayer16 = varData ['player'] [15] ['strPlayer']
    varBorn16 = varData ['player'][15]['dateBorn']
    varPosition16 = varData ['player'][15]['strPosition']
    varNationality16 = varData ['player'][15]['strNationality']
    varDescription16 = varData ['player'][15]['strDescriptionEN']
        
    openWeb = input("Would you like to open this information in a webpage? y/n \n")

    if openWeb == "y":
            
        writeHTML(varPlayer16, varBorn16, varPosition16, varNationality16, varDescription16)

    elif openWeb == "n":

        print(" ")
        print("Thank you for using this program")
        print(" ")
        input("Press ENTER to quit the program")

    else:

        print(" ")
        print("Invalid Character Given")
        print(" ")
        input("Press ENTER to quit the program")

#––––––––––––––––––––––––––––– Sead Kolasinac –––––––––––––––––––––––––––––

elif varPlayer == "17":
    print(" ")
    print ("Selected Player: Sead Kolasinac")

    varData = request.json()
    varPlayer17 = varData ['player'] [16] ['strPlayer']
    varBorn17 = varData ['player'][16]['dateBorn']
    varPosition17 = varData ['player'][16]['strPosition']
    varNationality17 = varData ['player'][16]['strNationality']
    varDescription17 = varData ['player'][16]['strDescriptionEN']
        
    openWeb = input("Would you like to open this information in a webpage? y/n \n")

    if openWeb == "y":
            
        writeHTML(varPlayer17, varBorn17, varPosition17, varNationality17, varDescription17)

    elif openWeb == "n":

        print(" ")
        print("Thank you for using this program")
        print(" ")
        input("Press ENTER to quit the program")

    else:

        print(" ")
        print("Invalid Character Given")
        print(" ")
        input("Press ENTER to quit the program")

#–––––––––––––––––––––––– Konstantinos Mavropanos ––––––––––––––––––––––––

elif varPlayer == "18":
    print(" ")
    print ("Selected Player: Konstantinos Mavropanos")

    varData = request.json()
    varPlayer18 = varData ['player'] [17] ['strPlayer']
    varBorn18 = varData ['player'][17]['dateBorn']
    varPosition18 = varData ['player'][17]['strPosition']
    varNationality18 = varData ['player'][17]['strNationality']
    varDescription18 = varData ['player'][17]['strDescriptionEN']
        
    openWeb = input("Would you like to open this information in a webpage? y/n \n")

    if openWeb == "y":
            
        writeHTML(varPlayer18, varBorn18, varPosition18, varNationality18, varDescription18)

    elif openWeb == "n":

        print(" ")
        print("Thank you for using this program")
        print(" ")
        input("Press ENTER to quit the program")

    else:

        print(" ")
        print("Invalid Character Given")
        print(" ")
        input("Press ENTER to quit the program")

#––––––––––––––––––––––––––– Matteo Guendouzi –––––––––––––––––––––––––––

elif varPlayer == "19":
    print(" ")
    print ("Selected Player: Matteo Guendouzi")

    varData = request.json()
    varPlayer19 = varData ['player'] [18] ['strPlayer']
    varBorn19 = varData ['player'][18]['dateBorn']
    varPosition19 = varData ['player'][18]['strPosition']
    varNationality19 = varData ['player'][18]['strNationality']
    varDescription19 = varData ['player'][18]['strDescriptionEN']
        
    openWeb = input("Would you like to open this information in a webpage? y/n \n")

    if openWeb == "y":
            
        writeHTML(varPlayer19, varBorn19, varPosition19, varNationality19, varDescription19)

    elif openWeb == "n":

        print(" ")
        print("Thank you for using this program")
        print(" ")
        input("Press ENTER to quit the program")

    else:

        print(" ")
        print("Invalid Character Given")
        print(" ")
        input("Press ENTER to quit the program")

#–––––––––––––––––––––––––––– Lucas Torreira ––––––––––––––––––––––––––––

elif varPlayer == "20":
    print(" ")
    print ("Selected Player: Lucas Torreira")

    varData = request.json()
    varPlayer20 = varData ['player'] [19] ['strPlayer']
    varBorn20 = varData ['player'][19]['dateBorn']
    varPosition20 = varData ['player'][19]['strPosition']
    varNationality20 = varData ['player'][19]['strNationality']
    varDescription20 = varData ['player'][19]['strDescriptionEN']
        
    openWeb = input("Would you like to open this information in a webpage? y/n \n")

    if openWeb == "y":
            
        writeHTML(varPlayer20, varBorn20, varPosition20, varNationality20, varDescription20)

    elif openWeb == "n":

        print(" ")
        print("Thank you for using this program")
        print(" ")
        input("Press ENTER to quit the program")

    else:

        print(" ")
        print("Invalid Character Given")
        print(" ")
        input("Press ENTER to quit the program")

#––––––––––––––––––––––––––––– Unai Emery –––––––––––––––––––––––––––––

elif varPlayer == "21":
    print(" ")
    print ("Selected Player: Unai Emery")

    varData = request.json()
    varPlayer21 = varData ['player'] [20] ['strPlayer']
    varBorn21 = varData ['player'][20]['dateBorn']
    varPosition21 = varData ['player'][20]['strPosition']
    varNationality21 = varData ['player'][20]['strNationality']
    varDescription21 = varData ['player'][20]['strDescriptionEN']
        
    openWeb = input("Would you like to open this information in a webpage? y/n \n")

    if openWeb == "y":
            
        writeHTML(varPlayer21, varBorn21, varPosition21, varNationality21, varDescription21)

    elif openWeb == "n":

        print(" ")
        print("Thank you for using this program")
        print(" ")
        input("Press ENTER to quit the program")

    else:

        print(" ")
        print("Invalid Character Given")
        print(" ")
        input("Press ENTER to quit the program")

#–––––––––––––––––––––––––––– Nicolas Pepe ––––––––––––––––––––––––––––

elif varPlayer == "22":
    print(" ")
    print ("Selected Player: Nicolas Pepe")

    varData = request.json()
    varPlayer22 = varData ['player'] [21] ['strPlayer']
    varBorn22 = varData ['player'][21]['dateBorn']
    varPosition22 = varData ['player'][21]['strPosition']
    varNationality22 = varData ['player'][21]['strNationality']
    varDescription22 = varData ['player'][21]['strDescriptionEN']
        
    openWeb = input("Would you like to open this information in a webpage? y/n \n")

    if openWeb == "y":
            
        writeHTML(varPlayer22, varBorn22, varPosition22, varNationality22, varDescription22)

    elif openWeb == "n":

        print(" ")
        print("Thank you for using this program")
        print(" ")
        input("Press ENTER to quit the program")

    else:

        print(" ")
        print("Invalid Character Given")
        print(" ")
        input("Press ENTER to quit the program")

#–––––––––––––––––––––––––– Jherson Vergara ––––––––––––––––––––––––––

elif varPlayer == "23":
    print(" ")
    print ("Selected Player: Jherson Vergara")

    varData = request.json()
    varPlayer23 = varData ['player'] [22] ['strPlayer']
    varBorn23 = varData ['player'][22]['dateBorn']
    varPosition23 = varData ['player'][22]['strPosition']
    varNationality23 = varData ['player'][22]['strNationality']
    varDescription23 = varData ['player'][22]['strDescriptionEN']
        
    openWeb = input("Would you like to open this information in a webpage? y/n \n")

    if openWeb == "y":
            
        writeHTML(varPlayer23, varBorn23, varPosition23, varNationality23, varDescription23)

    elif openWeb == "n":

        print(" ")
        print("Thank you for using this program")
        print(" ")
        input("Press ENTER to quit the program")

    else:

        print(" ")
        print("Invalid Character Given")
        print(" ")
        input("Press ENTER to quit the program")

#–––––––––––––––––––––––––– Victor Alvarez ––––––––––––––––––––––––––

elif varPlayer == "24":
    print(" ")
    print ("Selected Player: Victor Alvarez")

    varData = request.json()
    varPlayer24 = varData ['player'] [23] ['strPlayer']
    varBorn24 = varData ['player'][23]['dateBorn']
    varPosition24 = varData ['player'][23]['strPosition']
    varNationality24 = varData ['player'][23]['strNationality']
    varDescription24 = varData ['player'][23]['strDescriptionEN']
        
    openWeb = input("Would you like to open this information in a webpage? y/n \n")

    if openWeb == "y":
            
        writeHTML(varPlayer24, varBorn24, varPosition24, varNationality24, varDescription24)

    elif openWeb == "n":

        print(" ")
        print("Thank you for using this program")
        print(" ")
        input("Press ENTER to quit the program")

    else:

        print(" ")
        print("Invalid Character Given")
        print(" ")
        input("Press ENTER to quit the program")

#––––––––––––––––––––––––– Maksim Belyayev –––––––––––––––––––––––––

elif varPlayer == "25":
    print(" ")
    print ("Selected Player: Maksim Belyayev")

    varData = request.json()
    varPlayer25 = varData ['player'] [24] ['strPlayer']
    varBorn25 = varData ['player'][24]['dateBorn']
    varPosition25 = varData ['player'][24]['strPosition']
    varNationality25 = varData ['player'][24]['strNationality']
    varDescription25 = varData ['player'][24]['strDescriptionEN']
        
    openWeb = input("Would you like to open this information in a webpage? y/n \n")

    if openWeb == "y":
            
        writeHTML(varPlayer25, varBorn25, varPosition25, varNationality25, varDescription25)

    elif openWeb == "n":

        print(" ")
        print("Thank you for using this program")
        print(" ")
        input("Press ENTER to quit the program")

    else:

        print(" ")
        print("Invalid Character Given")
        print(" ")
        input("Press ENTER to quit the program")