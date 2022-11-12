#import all the required library
import bs4
from bs4 import BeautifulSoup as bs
import requests

#Link of the website
link='https://www.flipkart.com/search?q=sony+headphones&sid=0pm%2Cfcn%2Cgc3%2Cka8&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=sony+headphones%7CWireless+Headphones&requestId=dd4bff95-b57d-4afa-9e3b-50a9e218f31c&as-backfill=on'

#sending HTTP request to the URL above
page = requests.get(link)

#printing the content of the page
page.content

#converting the data from one format to another
test1= bs(page.content, 'html.parser')

#it gives us the visual representation of data
print(test1.prettify())

#extracting the name of the headphones and storing in the c
name=test1.find('a',class_="s1Q9rs")
print(name)

# to get just the name we will use the below code
name.text

#get rating of a product
rating=test1.find('div',class_="gUuXy- _2D5lwg")
print(rating)
rating.text

#name of the products
products=test1.find('div',class_="_YokD2 _3Mn1Gg")
print(products)
products.text

#get other details and specifications of the product
specification=test1.find('div',class_="_2418kt")
print(specification)
specification.text

for each in specification:
    spec=each.find_all('li',class_="_1YokD2 _2GoDe3")
    print(spec[0].text)
    print(spec[1].text)
    print(spec[2].text)
    print(spec[4].text)
    print(spec[5].text)
    print(spec[7].text)


#get the price of the product
price=test1.find('div',class_="_25b18c")
print(price)
price.text

#Defining the list for all features
Mic=[]              #Avaibility of mic in headset
Bt_version=[]                #Bluetooth version
wireless_range= []                #wireless range of the headphones                
battery_life = []                  #battery life of the headphones
touch_controls = []               #Accessibility of controls


for data in test1.findAll('div',class_='2418kt'):
        names=data.find('div', attrs={'class':'s1Q9rs'})
        price=data.find('div', attrs={'_25b18c'})
        rating=data.find('div', attrs={'gUuXy- _2D5lwg'})
        specification = data.find('div', attrs={'_2418kt'})
        
        for each in specification:
            col=each.find_all('li', attrs={'class':'_2418kt'})
            Mic_=col[0].text
            Bt_version_= col[1].text
            battery_life_= col[2].text
            touch_controls_= col[3].text

products.append(names.text) # Add product name to list
price.append(price.text) # Add price to list
Mic.append(Mic_)# Add supported apps specifications to list
Bt_version.append(Bt_version_) # Add operating system specifications to list
battery_life.append(battery_life_) # Add resolution specifications to list
touch_controls.append(touch_controls_) # Add sound specifications to list
rating.append(rating.text)   #Add rating specifications to list

#printing the length of list
print(len(products))
print(len(rating))
print(len(price))
print(len(Mic))
print(len(Bt_version))
print(len(battery_life))
print(len(touch_controls))

import pandas as pd
df=pd.DataFrame({'Product Name':products,'Mic':Mic,'Bluetooth version':Bt_version,'Battery life':battery_life,"touch controls":touch_controls,'Price':price,'Rating':rating})
df.head(10)