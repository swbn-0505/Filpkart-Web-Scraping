import pandas as pd
import requests
from bs4 import BeautifulSoup

data = []

for num in range(2,12):
    url = "https://www.flipkart.com/search?q=mobile+phones+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(num)

    r = requests.get(url)

    soup = BeautifulSoup(r.text , "lxml")
    box = soup.find("div" , class_ = "DOjaWF gdgoEp")

    cards = box.find_all("div" , class_ = "tUxRFH")
    names = soup.find_all("div" , class_ = "KzDlHZ")
    prices = soup.find_all("div" , class_ = "Nx9bqj _4b5DiR")
    description = soup.find_all("ul" , class_ = "G4BRas")
    reviews = box.find_all("div" , class_ = "XQDdHH")
    # print(reviews)
    for card in cards:
        name_tag = card.find("div", class_="KzDlHZ")
        price_tag = card.find("div", class_="Nx9bqj _4b5DiR")
        desc_tag = card.find("ul", class_="G4BRas")
        review_tag = card.find("div", class_="XQDdHH")  

        product = {
            "Product Name": name_tag.text if name_tag else None,
            "Price": price_tag.text if price_tag else None,
            "Description": desc_tag.text if desc_tag else None,
            "Reviews": review_tag.text if review_tag else None
        }    

        data.append(product)
    print("Page " , num-1 , "Scrapped")

print("SCRAPPING COMPLETED SUCCESSFULLY")
df = pd.DataFrame(data)
# print(df)
df.to_csv("flipkart_mobiles_under_50000.csv")
print("flipkart_mobiles_under_50000.csv created successfully")

    # print(soup)
    # while(True):
    # np = soup.find("a" , class_ = "_9QVEpD").get("href")
    #     # print(np)
    # cnp = "https://www.flipkart.com"+np
    # print(cnp)

    # url = cnp

    # r = requests.get(url)
    # soup = BeautifulSoup(r.text , "lxml")