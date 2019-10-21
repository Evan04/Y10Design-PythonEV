import requests
import json
import pprint

def writeHTML(data):
    myfile = open("articleAPI.html","w")

    myfile.close()

def main():

    articleInput = int(input("Choose an article you would like more information about? \n"))

    if articleInput < 0:
        print("Invalid Number")

    article1 = int(input("1. Justice Department distances itself from Giuliani \n"))
    article2 = int(input("2. Mitt Romney Admits Using Secret 'Pierre Delecto' Twitter Account to Defend Himself \n"))
    article3 = int(input("3. A life-threatening situation’: Dallas tornado devastates homes, leaves thousands without power \n"))
    article4 = int(input("4. Trump’s Base Digs In Its Heels, Even as Support for Impeachment Grows \n"))
    article5 = int(input("5. '$50bn is pocket change': opioid makers on trial in Ohio after talks collapse \n"))
    article6 = int(input("6. The latest on the Trump impeachment inquiry: Live updates \n"))
    article7 = int(input("7. Boris Johnson pushes for Brexit vote after British Parliament's snub \n"))
    article8 = int(input("8. US Special Forces soldier wears BANNED Kurdish patch as troops pull out of Syria \n"))
    article9 = int(input("9. Military training accident leaves 3 soldiers dead \n"))
    article10 = int(input("10. Summit County to dismiss opioid claims against small distributor as other drug companies prepare for first federal trial \n"))

    if articleInput < 0:
        print("Invalid Number")

    else:
        print("What information do you want about the article?")
        print("1. Description")
        print("2. URL")
        print("3. Publish Date")
        print("4. Author")

        informationRequested = input("Please input all fields you want to see. Ensure there are no spaces between numbers.\n")

    myrequest = requests.get("https://gnews.io/api/v3/top-news?token=e5509443651c0842b01c9142e25ef5f0")

    data_json = myrequest.json()

    x = data_json['articleCount']
    print (x)

    y = data_json['timestamp']
    print (y)


    z = data_json['articles'][2]['url']
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(z)

main()