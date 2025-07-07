

from pprint import pprint
import pandas as pd
from bs4 import BeautifulSoup 
import requests

url = "https://www.flipkart.com/search?q=mobiles"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

mobiles = soup.find_all("div", attrs={"class": "tUxRFH"})
print(mobiles)

data = []  

for i in mobiles:
    name = i.find("div", attrs={"class": "KzDlHZ"})
    price = i.find("div", attrs={"class": "Nx9bqj _4b5DiR"})
    rating = i.find("div", attrs={"class": "XQDdHH"})
    review = i.find("span", class_="Wphh3N")
    image = i.find("img", class_="DByuf4")

    data.append({
        "Name": name,
        "Price": price.text,
        "Rating": rating.text,
        "Review Count": review,
        "Image URL": image["src"]
    })

pprint(data)

df = pd.DataFrame(data)
df.to_csv("flipkart_mobiles.csv", index=False)
print("Saved to CSV: flipkart_mobiles.csv")
