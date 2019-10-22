import requests
import json
import pprint

def generalInfo():

    global request, jsonData

    response = requests.get("https://geo-info.co/43.65,-79.40")

    if (response.status_code == 200):
        request = requests.get("https://gnews.io/api/v3/top-news?token=e5509443651c0842b01c9142e25ef5f0")

        jsonData = request.json()

        numArticles = jsonData['articleCount']
        print(str(numArticles)+" articles were counted.")

    else:
        print("An error has occured.")

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

    articleOption = 0

    #********************* Articles 1 **********************

    if articleInput == 1:
        print(" ")
        print("Selected: Justice Department distances itself from Giuliani")
        print(" ")
        print("1. Description")
        print(" ")
        print("2. URL")
        print(" ")
        print("3. Published Date")
        print(" ")
        print("4. Author")
        print(" ")
        print("Please Make Your Selection")

        articleOption = float(input("  \n"))

        if articleOption == 1:
            print("descripton here")

        elif articleOption == 2:
            print("url here")

        elif articleOption == 3:
            print("published date here")

        elif articleOption == 4:
            print("author here")

#********************* Articles 2 **********************

    if articleInput == 2:
        print(" ")
        print("Selected: Mitt Romney Admits Using Secret 'Pierre Delecto' Twitter Account to Defend Himself")
        print(" ")
        print("1. Description")
        print(" ")
        print("2. URL")
        print(" ")
        print("3. Published Date")
        print(" ")
        print("4. Author")
        print(" ")
        print("Please Make Your Selection")

        articleOption = float(input("  \n"))

        if articleOption == 1:
            print("descripton here")

        elif articleOption == 2:
            print("url here")

        elif articleOption == 3:
            print("published date here")

        elif articleOption == 4:
            print("author here")

#********************* Articles 3 **********************

    if articleInput == 3:
        print(" ")
        print("Selected: 'A life-threatening situation’: Dallas tornado devastates homes, leaves thousands without power")
        print(" ")
        print("1. Description")
        print(" ")
        print("2. URL")
        print(" ")
        print("3. Published Date")
        print(" ")
        print("4. Author")
        print(" ")
        print("Please Make Your Selection")

        articleOption = float(input("  \n"))

        if articleOption == 1:
            print("descripton here")

        elif articleOption == 2:
            print("url here")

        elif articleOption == 3:
            print("published date here")

        elif articleOption == 4:
            print("author here")

#********************* Articles 4 **********************

    if articleInput == 4:
        print(" ")
        print("Selected: Trump’s Base Digs In Its Heels, Even as Support for Impeachment Grows")
        print(" ")
        print("1. Description")
        print(" ")
        print("2. URL")
        print(" ")
        print("3. Published Date")
        print(" ")
        print("4. Author")
        print(" ")
        print("Please Make Your Selection")

        articleOption = float(input("  \n"))

        if articleOption == 1:
            print("descripton here")

        elif articleOption == 2:
            print("url here")

        elif articleOption == 3:
            print("published date here")

        elif articleOption == 4:
            print("author here")

#********************* Articles 5 **********************

    if articleInput == 5:
        print(" ")
        print("Selected: '$50bn is pocket change': opioid makers on trial in Ohio after talks collapse")
        print(" ")
        print("1. Description")
        print(" ")
        print("2. URL")
        print(" ")
        print("3. Published Date")
        print(" ")
        print("4. Author")
        print(" ")
        print("Please Make Your Selection")

        articleOption = float(input("  \n"))

        if articleOption == 1:
            print("descripton here")

        elif articleOption == 2:
            print("url here")

        elif articleOption == 3:
            print("published date here")

        elif articleOption == 4:
            print("author here")


        


generalInfo()