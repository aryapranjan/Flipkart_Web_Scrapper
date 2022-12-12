from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

link='https://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_2_na_na_na&as-pos=2&as-type=RECENT&suggestionId=iphone%7CMobiles&requestId=1d8c8292-42b1-4042-b8e6-d22e20ee1b81&as-searchtext=ip'
page = requests.get(link)
soup = bs(page.content, 'html.parser')

price=soup.find('div',class_="_30jeq3 _1_WHN1")
print(price.text)

name=soup.find('div',class_="_4rR01T")
print(name.text)

specs=soup.find('div',class_="fMghEO")
print(specs.text)

Rating=soup.find('div',class_="_3LWZlK")
print(Rating.text)

prices=[]
names=[]
specifications=[]
ratings=[]


for data in soup.findAll('div',class_='_1AtVbE col-12-12'):

    name = data.find('div', attrs={'class':'_4rR01T'})
    if name is not None:
        names.append(name.text) # Add price to list
    else:
        names.append("NULL")

    price = data.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    if price is not None:
        prices.append(price.text) # Add product name to list
    else:
        prices.append("NULL")

    rating = data.find('div', attrs={'class':'_3LWZlK'})
    if rating is not None:
        ratings.append(rating.text)
    else:
        ratings.append("NULL")

    specification = data.find('div', attrs={'class':'fMghEO'})
    if specification is not None:
        specifications.append(specification.text)
    else:
        specifications.append("NULL")

#printing the length of lists
print(len(prices))
print(len(names))
print(len(specifications))
print(len(ratings))


df=pd.DataFrame({'Product Name':names,'Price':prices,'Specs':specifications,'Ratings':ratings})
df.head(30)
