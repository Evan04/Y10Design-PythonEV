import requests
import json
import pprint

def writeHTML(data):
    myfile = open("articleAPI.html","w")

    myfile.close()

def main():

    print("List of Articles")
    print(" ")
    print("1. Justice Department distances itself from Giuliani")
    print(" ")
    print("2. Mitt Romney Admits Using Secret 'Pierre Delecto' Twitter Account to Defend Himself")
    print(" ")
    print("3. 'A life-threatening situation’: Dallas tornado devastates homes, leaves thousands without power")
    print(" ")
    print("4. Trump’s Base Digs In Its Heels, Even as Support for Impeachment Grows")
    print(" ")
    print("5. '$50bn is pocket change': opioid makers on trial in Ohio after talks collapse")
    print(" ")

    #********************** Variables **********************

    articleInput = int(input("Choose an article you would like more information about? \n"))

    articleDescription1 = 0

    articleDescription2 = 0

    articleDescription3 = 0

    articleDescription4 = 0

    articleDescription5 = 0



    #********************** Articles ***********************

    if articleInput == 1:
        articleDescription1 = int(input("1. Description \n"))
        articleAuthor1 = int(input("2. Author \n"))
        articlePublishedDate1 = int(input("3. Published Date \n"))
        articleURL1 = int(input("4. URL \n"))

        if articleDescription1 == 1:
            print("description")
        


main()