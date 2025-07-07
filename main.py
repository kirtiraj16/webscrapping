# # print("Web scraping started...")
# from pprint import pp
# import pandas as pd
# from bs4 import BeautifulSoup 
# import requests



# url = "https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
 
# mobiles = soup.find_all("div", attrs={"class":"tUxRFH"})
# print(mobiles)


# for i in mobiles:
#     name = i.find("div", attrs={"class":"KzDlHZ"}).text
#     price = i.find("div", attrs={"class":"Nx9bqj _4b5DiR"}).text
#     rating = i.find("div", attrs={"class":"XQDdHH"}).text 
#     review_text = i.find("span", class_="Wphh3N").text.strip()
#     review_count = review_text.split('&')[-1].strip().replace("Reviews", "").strip()
#     image_url = i.find("img", class_="DByuf4")["src"] if i.find("img") else "No Image"
    
#     mob_data = {
#         "Name": name,
#         "Price": price,
#         "Rating": rating,
#         "Review Count": review_count,
#         "Image URL": image_url
#         }
#     mobiles.append(mob_data)
    
# pp.print(mobiles)

# df = pd.DataFrame(mobiles)
# print(df)
# df.to_csv("flipkart_mobiles.csv", index=False)
# print("Saved to CSV: flipkart_mobiles.csv")



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
