import requests
from bs4 import BeautifulSoup
import pandas as pd
Product_Name=[]
Prices=[]
Images=[]
url="https://www.nike.com/in/w?q=air%20jordan%20shoes&vst=air%20jordan%20shoes"
r=requests.get(url)
soup=BeautifulSoup(r.text,"lxml")
names=soup.find_all("div",class_="product-card__title")
for i in names:
    name=i.text
    Product_Name.append(name)
print(len(Product_Name))    
prices=soup.find_all("div",class_="product-price__wrapper css-1q1feg0")
for i in prices:
    price=i.text
    Prices.append(price)
    
df=pd.DataFrame({"Product Name":Product_Name,"Prices":Prices})
print(df)
df.index+=1
df.index
df.to_csv("nike website.csv")